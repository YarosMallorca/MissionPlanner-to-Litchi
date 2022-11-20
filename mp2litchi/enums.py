"""
Module to bundle all enum classes
"""
from enum import Enum


class MPCommand(Enum):
    """
    Enum class for the command ids of mission planner waypoint export files
    """

    WAYPOINT = 16
    SPLINE_WAYPOINT = 82
    LOITER_TURNS = 18
    LOITER_TIME = 19
    LOITER_UNLIM = 17
    RTL = 20
    LAND = 21
    TAKEOFF = 22
    DELAY = 93
    GUIDED_ENABLE = 92
    PAYLOAD_PLACE = 94
    DO_GUIDED_LIMITS = 222
    DO_WINCH = 42600
    DO_SET_ROI = 201
    CONDITION_DELAY = 112
    CONDITION_CHANGE_ALT = 113
    CONDITION_DISTANCE = 114
    CONDITION_YAW = 115
    DO_JUMP = 177
    DO_CHANGE_SPEED = 178
    DO_GRIPPER = 211
    DO_PARACHUTE = 208
    DO_SET_CAM_TRIG_DISTANCE = 206
    DO_SET_RELAY = 181
    DO_REPEAT_RELAY = 182
    DO_SET_SERVO = 183
    DO_REPEAT_SERVO = 184
    DO_DIGICAM_CONFIGURE = 202
    DO_DIGICAM_CONTROL = 203
    DO_MOUNT_CONTROL = 205
    DO_SPRAYER = 216


class InfoMessage(Enum):
    """
    Enum class for info messages to be shows in the gui or log
    """
    NO_SPEED_SET = 'No speed is set. Using Cruising Speed setting in litchi.'


class WarningMessage(Enum):
    """
    Enum class for warning messages to be shows in the gui or log
    """

    SPEED_CAP = 'The speed has been set to 15m/s due to Litchi limitations.'
    SPEED_NEGATIVE = 'The speed has been set to cruise speed ' \
                     '(see Litchi settings) because negative speed is not allowed.'


class ErrorMessage(Enum):
    """
    Enum class for error messages to be shows in the gui or log
    """

    FILE_NOT_FOUND = 'The file was not found.'
