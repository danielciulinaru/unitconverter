from .functions import extract_numeral_and_units


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

    def __init__(
            self,
            precision=0,
            default_unit="MB",
            spaced_units=False,
    ):
        self.precision = precision
        self.default_unit = default_unit
        self.spaced_units = spaced_units

    def convert(self, identifier, intended_unit=None):
        self.identifier = identifier
        if intended_unit:
            self.intended_unit = intended_unit
        else:
            self.intended_unit = self.default_unit
        self.converted_unit = self.intended_unit
        self.validated_numeral, self.validated_unit = extract_numeral_and_units(
            self.identifier, self.default_unit
        )
        return self.converted_numeral, self.converted_unit, self.converted_size
