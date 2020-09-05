from .constants import *


class UnitConverter(object):
    """
    class UnitConverter performs what it says: takes in an arbitrary number of *bytes and converts it in the intended
    unit, by calling its sole public method, convert()

    Example:
    initial = ' 523 GB '
    uc = UnitConverter()
    uc.truncate_decimals = True
    result_number, result_unit, result_size = uc.convert(initial, 'g')

    Legend:
        identifier = the input of the convert() function, a string in the format: 1 mb, 1m, 10MB, 10Mb. It can have
        leading and trailing spaces, as well as interspersed spaces
        validated_numeral = the number extracted from identifier, in float format
        validated_
    """
    from .descriptors import _Identifier
    from .descriptors import _UnitDescriptor
    from .descriptors import _NumeralDescriptor
    from .descriptors import _SizeDescriptor

    identifier = _Identifier()
    default_unit = _UnitDescriptor()
    intended_unit = _UnitDescriptor()
    converted_unit = _UnitDescriptor()
    validated_unit = _UnitDescriptor()
    validated_numeral = _NumeralDescriptor()
    converted_numeral = _NumeralDescriptor()
    validated_size = _SizeDescriptor()
    converted_size = _SizeDescriptor()
    default_rounding_decimals = 1

    def __init__(
            self,
            truncate_decimals=True,
            default_unit="MB",
            rounding_decimals=None,
            spaced_units=False,
    ):
        self.identifier = 1
        self.truncate_decimals = truncate_decimals
        self.default_unit = default_unit
        if rounding_decimals:
            self.rounding_decimals = rounding_decimals
        else:
            self.rounding_decimals = self.default_rounding_decimals
        if spaced_units:
            self.spaced_units = spaced_units

    def convert(self, identifier, intended_unit=None):
        self.identifier = identifier
        if intended_unit:
            self.intended_unit = intended_unit
        else:
            self.intended_unit = self.default_unit
        self.converted_unit = self.intended_unit
        self.validated_numeral, self.validated_unit = self.extract_numeral_and_units(
            self.identifier
        )
        return self.converted_numeral, self.converted_unit, self.converted_size

    def extract_numeral_and_units(self, value):
        _unitlist = []
        for letter in reversed(value):
            if letter.isdigit() is False:
                _unitlist.append(letter)
            elif letter.isdigit():
                break
        if _unitlist:
            _unitlist.reverse()
            unit = "".join(_unitlist)
        else:
            unit = self.normalize_unit()
        try:
            numeral = value.split(unit)[0]
        except ValueError:
            numeral = ""
            return numeral, unit
        else:
            return numeral, unit

    def normalize_unit(self, value: str = None) -> str:
        """ Normalize units to capital single letters. It's critical to use them in a standard format, due to the fact
            that the normalized units will be used to get the conversion power, in self._get_conversion_factor
            """
        y = STANDARD_UNIT_MB.upper()
        if value is None:
            return self.default_unit
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

    @staticmethod
    def get_conversion_power(source_unit, intended_unit):
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
