    **UnitConverter package**
    
    The goal of this package is to normalize and perform standard transformation of digital units.
    The original intent was to provide a standard format for the digital units used in an Oracle ecosystem (RMAN, sqlplus, etc) and these units come in the format of "120M" for 120 megabytes.
    
    class UnitConverter:
    - convert(): takes in a string representing information quantity and converts it in the intended unit
    - if convert() is called without an intended_unit, it uses the UnitConverter.default_unit as a destination transformation unit
    - the UnitConverter.default_unit defaults to megabytes or "M", if not passed to the constructor

    All units are normalized and displayed in a normalized short form.
    For example:
    - "mb" becomes "M"
    - "MB" becomes "M"
    - "Mb" becomes "M"
      
    Caveats:
    - as it stands currently, the transformation is done in base 1024, not 1000
    - there's no distinction between "MB" and "Mb", that is, between megabytes and megabits
    - there's no distinction between megabytes and mebibytes. All transformations are done in 1024 base, but still represented as megabytes. This is done for convenience purposes.

    Usage example:
    from unitconverter import UnitConverter as UC
    uc = UC()
    uc.convert("2048kb")

    # increase precision so you could have more decimals after the dot
    from unitconverter import UnitConverter as UC
    uc = UC(precision=3, default_unit='g')
    uc.convert("204mb")
    (Decimal('0.199'), 'G', '0.199G')
    
    # UC.spaced_units = True puts a space between the numeral and its accompanying
    # unit
    from unitconverter import UnitConverter as UC
    uc = UC(spaced_units=True)
    uc.convert("204mb")
    (Decimal('204'), 'M', '204 M')
    
    # You can capture the conversion result via tuple expansion:
    from unitconverter import UnitConverter as UC
    uc = UC(precision=3, default_unit='g')
    numeral, unit, size = uc.convert("248m")
    print(f"{numeral}, {unit}, {size}")
    0.242, G, 0.242G
    
    # Perform conversion but also use methods chaining:
    from unitconverter import UnitConverter as UC
    uc = UC()
    uc.set_spaced_unit(True).set_precision(3).convert("248mb", "g")
    (Decimal('0.242'), 'G', '0.242 G')
