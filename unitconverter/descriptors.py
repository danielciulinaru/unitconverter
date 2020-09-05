from .exceptions import UnitConverterError
from .functions import is_digit
from .functions import is_unit
from .constants import FACTOR


class _NumeralDescriptor(object):
    """
    Numeral descriptor, handles the validation of numerals. Raises a UnitCheckError exception in case of an
    invalid numeral
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, numeral):
        if is_digit(numeral):
            self.__dict__[self.name] = float(numeral)
        else:
            msg = "parsing the numeral generated an empty value"
            raise UnitConverterError(msg)

    def __get__(self, instance, owner):
        if self.name == "converted_numeral":
            power = instance.get_conversion_power(
                instance.validated_unit, instance.intended_unit
            )
            converted_result = float(instance.validated_numeral * (FACTOR ** power))
            if instance.truncate_decimals is True:
                return int(round(converted_result, 0))
            elif instance.truncate_decimals is False:
                return round(converted_result, instance.rounding_decimals)
        elif self.name == "validated_numeral":
            return self.__dict__[self.name]


class _UnitDescriptor(object):
    """
    Descriptor, it encapsulates the verification of units, performed with is_unit(). It raises a UnitCheckError
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
        self.__dict__[self.name] = instance.normalize_unit(work_unit)

    def __get__(self, instance, owner):
        return self.__dict__[self.name]

    def __delete__(self, instance):
        del self.__dict__[self.name]


class _SizeDescriptor(object):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if hasattr(instance, "spaced_units") and instance.spaced_units is True:
            if self.name == "validated_size":
                return f"{instance.validated_numeral} {instance.validated_unit}"
            elif self.name == "converted_size":
                return f"{instance.converted_numeral} {instance.converted_unit}"
        else:
            if self.name == "validated_size":
                return f"{instance.validated_numeral}{instance.validated_unit}"
            elif self.name == "converted_size":
                return f"{instance.converted_numeral}{instance.converted_unit}"


class _Identifier(object):
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, identifier):
        if identifier is None or identifier is False:
            raise UnitConverterError(numeral=identifier)
        else:
            self.__dict__[self.name] = (
                str(identifier).replace(",", "").strip().replace(" ", "")
            )

    def __get__(self, instance, owner):
        return self.__dict__[self.name]
