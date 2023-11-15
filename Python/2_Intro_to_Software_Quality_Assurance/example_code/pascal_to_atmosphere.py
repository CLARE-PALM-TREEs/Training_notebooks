from numbers import Number

def pascal_to_atmosphere(pascal):
    """
    >>> pressure_in_pascal = 97348.0
    >>> pressure_in_atmosphere = pascal_to_atmosphere(pressure_in_pascal)
    >>> assert round(pressure_in_atmosphere, 2) == 0.96
    """
    if not isinstance(pascal, Number):
        raise TypeError('Please provide a numerical value')
    atmosphere = float(pascal / 101325.0)
    return atmosphere
    
