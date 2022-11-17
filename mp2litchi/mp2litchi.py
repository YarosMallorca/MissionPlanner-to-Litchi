"""
Mission Planner to Litchi Converter by https://github.com/YarostheLaunchpadder
"""
import os

from litchi_wp.enums import AltitudeMode
from litchi_wp.waypoint import Waypoint

from mp2litchi.enums import MPCommand
from mp2litchi.global_mp_cmd import GlobalMPCmdManager


def welcome():
    """
    Welcome messages
    """
    print("WELCOME TO MISSION PLANNER TO LITCHI CONVERTER!\n")
    print("Converted files will be saved to the same directory the source file is in.\n")


def parse_file(filename: str) -> list[list[str]]:
    """
    Reads File and converts it to a list of single values
    @param filename: The path to the file. e.g.: /home/user/any/file.waypoints
    @return: A List with sublists each containing the values of each line extracted from the file
    """
    if not filename.endswith(".waypoints"):
        filename += ".waypoints"

    # convert to list of single values
    with open(filename, "r", encoding='utf-8') as file_handle:
        file = file_handle.read()
    file = str(file.split("\t"))
    file = file.replace("\\n", "', '")
    file = file.replace("'", "")
    file_list = file.strip('][').split(', ')
    if 'WPL' in file_list[0]:
        del file_list[0]  # remove header
    file_lists = [  # pack each line into a sublist
        file_list[x:x + 12] for x in range(0, len(file_list), 12)
    ]
    return file_lists


def get_cmd(lst: list[str]) -> MPCommand | None:
    """
    Extracts the command from a mp waypoint line
    """
    try:
        return MPCommand(
            int(float(
                lst[3]
            ))
        )
    except (ValueError, IndexError):
        return None


def convert(filename: str, set_agl=True):
    """
    Converts a single file
    :param filename: The path to the file. e.g.: /home/user/any/file.waypoints
    :param set_agl: Sets the AGL flag of the waypoints if True
    """
    while not os.path.exists(filename):
        filename = input("\nCouldn't find path to Mission Planner file, please try again: ")

    receiver_cmds = [MPCommand.WAYPOINT]  # mp commands that can be referenced by action commands
    file_list = parse_file(filename)
    globalCmdManager = GlobalMPCmdManager()
    waypoint_list = []
    temp_wp: Waypoint | None = None
    after_takeoff = False

    for row in file_list:
        if not after_takeoff:
            if get_cmd(row) is MPCommand.TAKEOFF:  # ignore anything before takeoff
                after_takeoff = True
            continue
        if get_cmd(row) in receiver_cmds:
            if temp_wp is not None:
                waypoint_list.append(temp_wp)  # store waypoint
            latitude = float(row[8])  # latitude is at location 8
            longitude = float(row[9])  # longitude  is at location 9
            altitude = float(row[10])  # altitude  is at location 10
            altitude_mode = AltitudeMode.AGL if set_agl else AltitudeMode.MSL
            temp_wp = Waypoint(lat=latitude, lon=longitude, alt=altitude)  # create new waypoint
            temp_wp.set_altitude(value=altitude, mode=altitude_mode)  # set the altitude mode
            globalCmdManager.apply_all_active_to_waypoint(waypoint=temp_wp)  # apply all active global commands to wp
        else:  # not a command receiver. Be careful temp_wp might be None
            command = get_cmd(row)
            global_cmd = globalCmdManager.is_global(command)
            if global_cmd:
                param = float(row[global_cmd.param_loc])
                globalCmdManager.update(command, param)
                if temp_wp:
                    globalCmdManager.apply_to_waypoint(global_cmd, waypoint=temp_wp)
            else:
                # handle all non-global commands
                pass
        if file_list.index(row) == len(file_list) - 1:  # is last row
            waypoint_list.append(temp_wp)  # store waypoint
            temp_wp = None

    output_string = Waypoint.get_header()
    for wpoint in waypoint_list:
        output_string += wpoint.to_line()

    with open(f"{filename}.csv", "w", encoding='utf-8') as output_file:
        output_file.write(output_string)
        output_file.close()

    print(f"\nFile saved: {filename}.csv")
