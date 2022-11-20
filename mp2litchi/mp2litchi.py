"""
Mission Planner to Litchi Converter by https://github.com/YarostheLaunchpadder
"""
import os
from typing import Tuple

from litchi_wp.enums import AltitudeMode, ActionType
from litchi_wp.waypoint import Waypoint

from mp2litchi.enums import MPCommand, WarningMessage, ErrorMessage
from mp2litchi.global_mp_cmd import GlobalMPCmdManager


def welcome():
    """
    Welcome messages
    """

    print("WELCOME TO MISSION PLANNER TO LITCHI CONVERTER!\n")
    print("Converted files will be saved to the same directory the source file is in.\n")


def parse_file(filename: str) -> list[list[str]]:
    """

    Args:
        filename (str): The path to the file. e.g.: /home/user/any/file.waypoints

    Returns:
        A List with sublists each containing the values of each line extracted from the file

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


def get_delay(line: list[str]) -> float:
    """
    Extracts the delay from a waypoint

    Args:
        line (list[str]): The Line to be parsed

    Returns:
        The delay in seconds (float)

    """

    return float(line[4])


def check_valid_line(line: list[str]) -> bool:
    """
    Checks if the line is valid
    (better use regexp https://www.w3schools.com/python/python_regex.asp))

    Args:
        line (list[str]): The line to be checked

    Returns:
        True if line passed the checks

    """

    if len(line) != 12:  # invalid lines
        return False
    return True


# pylint: disable=too-many-locals,too-many-branches,too-many-statements
# (better split function so pylint is happy)
def convert(filename: str, set_agl=True) -> Tuple[list[str], list[str], list[str]]:
    """
    Converts a single file
    Args:
        filename (str): The path to the file. e.g.: /home/user/any/file.waypoints
        set_agl (bool): Sets the AGL flag of the waypoints if True

    Returns:
        A tuple of (info, warning, error) messages

    """

    infos: list[str] = []  # List of info messages
    warnings: list[str] = []  # List of warning messages
    errors: list[str] = []  # List of error messages
    if not os.path.exists(filename):
        errors.append(ErrorMessage.FILE_NOT_FOUND.value)

    receiver_cmds = [MPCommand.WAYPOINT]  # mp commands that can be referenced by action commands
    file_list = parse_file(filename)
    global_cmd_manager = GlobalMPCmdManager()
    waypoint_list: list[Waypoint] = []
    temp_wp: Waypoint | None = None

    for row in file_list:
        if not check_valid_line(row):  # skip invalid lines
            continue
        if row[1] == '1':  # skip home location
            continue
        if get_cmd(row) is MPCommand.TAKEOFF:  # ignore any waypoints before takeoff
            waypoint_list.clear()
            continue
        if get_cmd(row) in receiver_cmds:
            if temp_wp is not None:
                waypoint_list.append(temp_wp)  # store waypoint
            action_index = 0
            latitude = float(row[8])  # latitude is at location 8
            longitude = float(row[9])  # longitude  is at location 9
            altitude = float(row[10])  # altitude  is at location 10
            altitude_mode = AltitudeMode.AGL if set_agl else AltitudeMode.MSL
            temp_wp = Waypoint(lat=latitude, lon=longitude, alt=altitude)  # create new waypoint
            temp_wp.set_altitude(value=altitude, mode=altitude_mode)  # set the altitude mode
            stay_for = get_delay(row)
            if stay_for > 0:  # is delay is set for waypoint
                temp_wp.set_action(  # set stay_for
                    index=action_index,
                    actiontype=ActionType.STAY_FOR,
                    param=int(stay_for * 1000)
                )
                action_index += 1
            global_cmd_manager.apply_all_active_to_waypoint(
                waypoint=temp_wp
            )  # apply all active global commands to wp
        else:  # not a command receiver. Be careful temp_wp might be None
            command = get_cmd(row)
            if command is None:  # skip invalid commands
                continue
            global_cmd = global_cmd_manager.is_global(command)
            if global_cmd:
                param = float(row[global_cmd.param_loc])
                if command is MPCommand.DO_CHANGE_SPEED:
                    if param > 15.0:
                        param = 15.0  # Litchi limits speed to 15 m/s max
                        warnings.append(
                            f"Line {file_list.index(row)}: {WarningMessage.SPEED_CAP.value}"
                        )
                    elif param < 0.0:
                        param = 0  # no negative speed in Litchi, replace with cruise speed
                        warnings.append(
                            f"Line {file_list.index(row)}: {WarningMessage.SPEED_NEGATIVE.value}"
                        )
                global_cmd_manager.update(command, param)
                if temp_wp:
                    global_cmd_manager.apply_to_waypoint(global_cmd, waypoint=temp_wp)
            else:
                # handle all non-global commands
                match command:
                    case MPCommand.DO_DIGICAM_CONTROL:
                        if temp_wp:
                            temp_wp.set_action(
                                index=action_index,
                                actiontype=ActionType.TAKE_PHOTO,
                            )
                            action_index += 1

        if file_list.index(row) == len(file_list) - 1:  # is last row
            waypoint_list.append(temp_wp)  # store waypoint
            temp_wp = None

    output_string = Waypoint.get_header()
    for waypoint in waypoint_list:
        output_string += waypoint.to_line()

    with open(f"{filename}.csv", "w", encoding='utf-8') as output_file:
        output_file.write(output_string)
        output_file.close()

    print(f"\nFile saved: {filename}.csv")
    return infos, warnings, errors
