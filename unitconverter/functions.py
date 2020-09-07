from decimal import InvalidOperation
from typing import Tuple

from .constants import *
from .exceptions import UnitConverterError


def is_digit(value: Digit) -> Union[Decimal, bool]:
    """
    Determine if value is an all digit. If the incoming x is a float, eliminate the dot and attempt
    to convert it to integer.
    Python's isdigit() does not handle Decimal numbers, hence the need for the current function
    """
    try:
        result = Decimal(value)
    except InvalidOperation:
        return False
    else:
        return result


def is_unit(value: AnyStr) -> Union[AnyStr, bool]:
    """
    Determine if the incoming argument is a valid unit
    """
    if str(value).lower() not in UNITS_LIST:
        return False
    else:
        return value


def extract_numeral_and_units(identifier: AnyStr, default_unit: AnyStr) -> Tuple[Digit, AnyStr]:
    _unitlist: List = []
    _unit: str = ""
    msg: str = "parsing the numeral generated an invalid value"

    # parse the incoming string in reverse and check if it's a possible numeral
    # use the is_digit() function that attempts a conversion to Decimal
    identifier = identifier.replace(" ", "")
    for letter in reversed(identifier):
        if is_digit(letter) is False:
            _unitlist.insert(0, letter)
        elif is_digit(letter):
            # found the first digit in the incoming value therefore exit the loop
            break
    _unit = "".join(_unitlist)
    _numeral = ""

    if len(_unitlist) == 0:
        """
        The unit string is empty, therefore allocate the default unit
        Validate the numeral that it can be a decimal
        """
        _unit = default_unit
        _numeral = is_digit(identifier)
        if _numeral is False:
            raise UnitConverterError(numeral=identifier, message=msg)
    else:
        """
        The unit string has a value, therefore proceed to split the incoming value by the unit string and extract
        the numeral.
        At the end also normalize the unit value as well
        """
        _result: str = ""
        try:
            _result = identifier.split(_unit)[0]
        except ValueError:
            raise UnitConverterError(_result)
        else:
            _numeral = is_digit(_result)
            if _numeral is False:
                raise UnitConverterError(numeral=_result, message=msg)
    return _numeral, _unit


def normalize_unit(value: AnyStr) -> AnyStr:
    """
    Normalize units to capital single letters. It's critical to use them in a standard format, due to the fact
    that the normalized units will be used to get the conversion power, in self._get_conversion_factor
    """
    # value = is_unit(value.replace(" ", ""))
    y = STANDARD_UNIT_MB.upper()
    if value.lower() in UNITS_B:
        y = STANDARD_UNIT_B
    elif value.lower() in UNITS_KB:
        y = STANDARD_UNIT_KB
    elif value.lower() in UNITS_MB:
        y = STANDARD_UNIT_MB
    elif value.lower() in UNITS_GB:
        y = STANDARD_UNIT_GB
    elif value.lower() in UNITS_TB:
        y = STANDARD_UNIT_TB
    elif value.lower() in UNITS_PB:
        y = STANDARD_UNIT_PB
    return y


def get_conversion_power(source_unit: AnyStr, intended_unit: AnyStr) -> int:
    """ Determines the conversion power for the 1024 base, between incoming unit and destination unit
        Functions according to this table:
             b 	        k 			m 			g 			t           p
        b   1024^0      1024^-1     1024^-2     1024^-3     1024^-4     1024^-5
        k   1024^1      1024^0 		1024^-1 	1024^-2 	1024^-3     1024^-4
        m   1024^2      1024^1		1024^0		1024^-1		1024^-2     1024^-3
        g   1024^3      1024^2		1024^1		1024^0		1024^-1     1024^-2
        t   1024^4      1024^3		1024^2		1024^1		1024^0      1024^-1
        p   1024^5      1024^4      1024^3      1024^2      1024^1      1024^0
        """
    matrix = [
        (STANDARD_UNIT_B, STANDARD_UNIT_B, 0),
        (STANDARD_UNIT_B, STANDARD_UNIT_KB, -1),
        (STANDARD_UNIT_B, STANDARD_UNIT_MB, -2),
        (STANDARD_UNIT_B, STANDARD_UNIT_GB, -3),
        (STANDARD_UNIT_B, STANDARD_UNIT_TB, -4),
        (STANDARD_UNIT_B, STANDARD_UNIT_PB, -5),
        (STANDARD_UNIT_KB, STANDARD_UNIT_KB, 0),
        (STANDARD_UNIT_KB, STANDARD_UNIT_MB, -1),
        (STANDARD_UNIT_KB, STANDARD_UNIT_GB, -2),
        (STANDARD_UNIT_KB, STANDARD_UNIT_TB, -3),
        (STANDARD_UNIT_MB, STANDARD_UNIT_KB, 1),
        (STANDARD_UNIT_MB, STANDARD_UNIT_MB, 0),
        (STANDARD_UNIT_MB, STANDARD_UNIT_GB, -1),
        (STANDARD_UNIT_MB, STANDARD_UNIT_TB, -2),
        (STANDARD_UNIT_GB, STANDARD_UNIT_KB, 2),
        (STANDARD_UNIT_GB, STANDARD_UNIT_MB, 1),
        (STANDARD_UNIT_GB, STANDARD_UNIT_GB, 0),
        (STANDARD_UNIT_GB, STANDARD_UNIT_TB, -1),
        (STANDARD_UNIT_TB, STANDARD_UNIT_KB, 3),
        (STANDARD_UNIT_TB, STANDARD_UNIT_MB, 2),
        (STANDARD_UNIT_TB, STANDARD_UNIT_GB, 1),
        (STANDARD_UNIT_TB, STANDARD_UNIT_TB, 0),
        (STANDARD_UNIT_PB, STANDARD_UNIT_B, 5),
        (STANDARD_UNIT_PB, STANDARD_UNIT_KB, 4),
        (STANDARD_UNIT_PB, STANDARD_UNIT_MB, 3),
        (STANDARD_UNIT_PB, STANDARD_UNIT_GB, 2),
        (STANDARD_UNIT_PB, STANDARD_UNIT_TB, 1),
        (STANDARD_UNIT_PB, STANDARD_UNIT_PB, 0),
    ]
    for item in matrix:
        if item[0] == source_unit and item[1] == intended_unit:
            return item[2]
