from .constants import POWERFACTOR
from .exceptions import UnitConverterError
from .functions import is_unit, normalize_unit, get_conversion_power


class _NumeralDescriptor(object):
    """
    Numeral descriptor:
    - handles the conversion of the numeral based on the power factor called POWERFACTOR
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, numeral):
        self.__dict__[self.name] = numeral

    def __get__(self, instance, owner):
        if self.name == "converted_numeral":
            power = get_conversion_power(
                instance.validated_unit, instance.intended_unit
            )
            converted_result = instance.validated_numeral * (POWERFACTOR ** power)
            return round(converted_result, instance.precision)
        elif self.name == "validated_numeral":
            return self.__dict__[self.name]


class _UnitDescriptor(object):
    """
    Unit descriptor:
    - it encapsulates the verification of units, performed with is_unit(). It raises a UnitConverterError
    exception in case of an invalid unit that's not part of the UNITS_LIST
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, unit):
        work_unit = str(unit).replace(" ", "").strip()
        if self.name == "intended_unit":
            if is_unit(work_unit) is False:
                raise UnitConverterError(intended_unit=unit)
        elif self.name == "default_unit":
            if is_unit(work_unit) is False:
                raise UnitConverterError(default_unit=unit)
        elif self.name == "validated_unit":
            if is_unit(work_unit) is False:
                raise UnitConverterError(validated_unit=unit)
        self.__dict__[self.name] = normalize_unit(work_unit)

    def __get__(self, instance, owner):
        return self.__dict__[self.name]

    def __delete__(self, instance):
        del self.__dict__[self.name]


class _SizeDescriptor(object):
    """
    Size descriptor:
    - handles the display of the SizeUnit variable, with or without spaces
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if hasattr(instance, "spaced_unit") and instance.spaced_unit is True:
            if self.name == "validated_size":
                return f"{instance.validated_numeral} {instance.validated_unit}"
            elif self.name == "converted_size":
                return f"{instance.converted_numeral} {instance.converted_unit}"
        else:
            if self.name == "validated_size":
                return f"{instance.validated_numeral}{instance.validated_unit}"
            elif self.name == "converted_size":
                return f"{instance.converted_numeral}{instance.converted_unit}"