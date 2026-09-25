"""
Exit codes for DevHealth CLI.
"""
from enum import IntEnum

class ExitCode(IntEnum):
    SUCCESS = 0
    WARNING = 1
    FAILURE = 2
    CONFIG_ERROR = 3