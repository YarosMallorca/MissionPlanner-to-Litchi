"""
Module for global MP commands
"""
from litchi_wp.waypoint import Waypoint

from mp2litchi.enums import MPCommand


# pylint: disable=too-few-public-methods
class GlobalMPCmd:
    """
    Represents a single MP cmd
    """

    def __init__(self, cmd: MPCommand, param: int | float = 0, active: bool = False, loc: int = 0):
        """
        Constructor

        Args:
            cmd (MPCommand): The MP command
            param (int | float): The parameter of the command
            active (bool): True if global command is active

        """

        self.active: bool = active
        self.type: MPCommand = cmd
        self.param: int | float = param
        self.param_loc: int = loc


class GlobalMPCmdManager:
    """
    Class for handling of global MP cmds

    Attributes:
        global_cmds (list[GlobalMPCmd]): List of commands that influence all following waypoints

    """

    global_cmds = [
        GlobalMPCmd(cmd=MPCommand.DO_CHANGE_SPEED, loc=5),
        GlobalMPCmd(cmd=MPCommand.DO_SET_CAM_TRIG_DISTANCE, loc=4)
    ]

    def get_active(self) -> list[GlobalMPCmd]:
        """
        Getter for all active global MP commands

        Returns:
            A list of GlobalMPCmd objects that are currently set to active

        """

        return [cmd for cmd in self.global_cmds if cmd.active]

    def apply_to_waypoint(self, cmd: GlobalMPCmd, waypoint: Waypoint):
        """
        Applies the global command to the waypoint
        Args:
            cmd: The command to be applied
            waypoint: The waypoint to be referenced

        """

        match cmd.type:
            case MPCommand.DO_SET_CAM_TRIG_DISTANCE:
                waypoint.set_photo_interval_distance(
                    round(cmd.param, 1)
                )
            case MPCommand.DO_CHANGE_SPEED:
                waypoint.set_speed_ms(
                    round(cmd.param, 2)
                )

    def apply_all_active_to_waypoint(self, waypoint: Waypoint):
        """
        Applies all active global commands to the Waypoint
        Args:
            waypoint: The waypoint to be referenced

        """

        cmds = self.get_active()
        for cmd in cmds:
            self.apply_to_waypoint(cmd, waypoint)

    def is_global(self, cmd: MPCommand) -> GlobalMPCmd | None:
        """
        Checks if a MP command has global effects

        Args:
            cmd: The MP command

        Returns:
            The command as GlobalMPCmd or None

        """

        for g_cmd in self.global_cmds:
            if g_cmd.type == cmd:
                return g_cmd
        return None

    def update(self, cmd: MPCommand, param: float | int) -> bool:
        """
        Checks if a given command has global effects.
        If that is the case the global command gets updated.

        Args:
            cmd: The MP command
            param: The Parameter of the command

        Returns:
            True if the command has global effects and was updated

        """

        for g_cmd in self.global_cmds:
            if g_cmd.type == cmd:
                g_cmd.param = param
                g_cmd.active = True
                return True
        return False
