class BaseTemplateError(Exception):
    def __init__(self, msg=""):
        self.msg = msg
        super().__init__(self.msg)

    def __repr__(self):
        return self.msg

    def __str__(self):
        self.__str__ = self.__repr__()
        return self.__str__


class UnitConverterError(BaseTemplateError):
    """ raised when a unit parsed by UnitConverter trips itself """

    def __init__(
            self,
            numeral=None,
            size_unit=None,
            validated_unit=None,
            intended_unit=None,
            default_unit=None,
            message="",
    ):
        if not message:
            if numeral:
                message = f"Numeral cannot be a non-digit or empty: {numeral}"
            if validated_unit:
                message = f"Extracted unit not in the approved list: {validated_unit}"
            if size_unit:
                message = f"Size unit not in the approved list: {size_unit}"
            if intended_unit:
                message = f"Intended unit not in the approved list: {intended_unit}"
            elif default_unit:
                message = f"Default unit not in the approved list: {default_unit}"
        self.message = message
        super().__init__(self.message)
