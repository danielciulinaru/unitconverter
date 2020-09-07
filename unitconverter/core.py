from .functions import extract_numeral_and_units


class UnitConverter(object):
    """
    class UnitConverter:
    - convert(): takes in a string representing information quantity and converts it in the intended
    unit
    - if convert() is called without an intended_unit, it uses the UnitConverter.default_unit as a destination
    transformation unit.
    - the UnitConverter.default_unit defaults to megabytes or "M"

    All units are normalized and displayed in a normalized short form.
    For example:
    - "mb" becomes "M"
    - "MB" becomes "M"
    - "Mb" becomes "M"

    Caveats:
    - as it stands currently, the transformation is done in base 1024, not 1000.
    - there's no distinction between "MB" and "Mb", that is megabytes and megabits
    - there's no distinction between megabytes and mebibytes. All transformations are done in 1024 base, but still
    represented as megabytes. This is done for convenience purposes.

    Usage example:
    from unitconverter import UnitConverter as UC
    uc = UC()
    uc.convert("2048kb")

    # increase precision so you could have more decimals after the dot
    uc = UC(precision=3, default_unit='g')
    uc.convert("204mb")

    """
    from .descriptors import _UnitDescriptor
    from .descriptors import _NumeralDescriptor
    from .descriptors import _SizeDescriptor

    indentifier: str
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
            spaced_unit=False,
    ):
        self.identifier = None
        self.precision = precision
        self.default_unit = default_unit
        self.spaced_unit = spaced_unit

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

    def set_precision(self, precision: int):
        self.precision = precision
        return self

    def set_spaced_unit(self, value: bool):
        self.spaced_unit = value
        return self
