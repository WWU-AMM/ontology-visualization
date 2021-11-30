import sys


def is_windows_platform():
    return sys.platform == 'win32' or sys.platform == 'cygwin'
