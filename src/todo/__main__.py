"""
The main entry point to the application.
"""

import enum
import sys
from typing import Sequence


class ExitCode(enum.IntEnum):
    """Describes the status of the program after it has terminated.

    Attributes
    ----------
    SUCCESS
        Terminated without any errors.
    FAILURE
        Terminated due to an unrecoverable error.
    USAGE
        Terminated due to invalid command-line arguments.
    """

    SUCCESS = 0
    FAILURE = 1
    USAGE = 2


def main(args: Sequence[str] = sys.argv[1:]) -> ExitCode:
    """The main entry point to the program.

    This function is intended to be wrapped by [`sys.exit`][sys.exit] so that
    its return value becomes the program's exit code.

    Parameters
    ----------
    args
        Command-line arguments.

    Returns
    -------
    ExitCode
        Zero indicates success; non-zero indicates failure.

    Notes
    -----
    The `args` parameter is primarily intended for testing. In normal usage,
    the program is installed with a wrapper script on `PATH` that calls this
    function without arguments.
    """
    print("Hello, World!")
    return ExitCode.SUCCESS


if __name__ == "__main__":
    sys.exit(main())
