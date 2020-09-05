from typing import Union
from .constants import UNITS_LIST


def is_digit(value: Union[str, float, int]):
    """
    Determine if value is an all digit. If the incoming x is a float, eliminate the dot and attempt
    to convert it to integer.
    Python's isdigit() does not handle float numbers, hence the need for the current function
    """
    checker = str(value).replace(".", "", 1)
    try:
        int(checker)
    except ValueError:
        return False
    else:
        return value


def is_unit(value: str):
    """
    Determine if the incoming argument is a valid unit
    """
    if str(value).lower() not in UNITS_LIST:
        return False
    else:
        return value
