"""
Mission Planner to Litchi Converter by https://github.com/YarostheLaunchpadder
"""
import os

from litchi_wp.waypoint import Waypoint
from litchi_wp.enums import AltitudeMode

from mp2litchi.enums import MPCommands


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


def get_cmd(lst: list[str]) -> MPCommands | None:
    """
    Extracts the command from a mp waypoint line
    """
    try:
        return MPCommands(
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

    cmd_receivers = [MPCommands.WAYPOINT]  # mp commands that can be referenced by action commands
    file_list = parse_file(filename)
    waypoint_list = []
    temp_wp: Waypoint | None = None
    after_takeoff = False

    for row in file_list:
        if not after_takeoff:
            if get_cmd(row) is MPCommands.TAKEOFF:  # ignore anything before takeoff
                after_takeoff = True
            continue
        if get_cmd(row) in cmd_receivers:
            if temp_wp is not None:
                waypoint_list.append(temp_wp)  # store waypoint
            latitude = float(row[8])  # latitude is at location 8
            longitude = float(row[9])  # longitude  is at location 9
            altitude = float(row[10])  # altitude  is at location 10
            altitude_mode = AltitudeMode.AGL if set_agl else AltitudeMode.MSL
            temp_wp = Waypoint(lat=latitude, lon=longitude, alt=altitude)  # create new waypoint
            temp_wp.set_altitude(value=altitude, mode=altitude_mode)  # set the altitude mode
        elif temp_wp is not None:
            match get_cmd(row):
                case MPCommands.DO_SET_CAM_TRIG_DISTANCE:
                    temp_wp.set_photo_interval_distance(
                        round(float(row[4]), 1)
                    )
                case MPCommands.DO_CHANGE_SPEED:
                    temp_wp.set_speed_ms(
                        round(float(row[5]), 2)
                    )
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
