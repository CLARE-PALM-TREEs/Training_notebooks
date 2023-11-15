from tests.common_funcs import assert_almost_equal
from pascal_to_atmosphere import pascal_to_atmosphere


def test_pascal_to_atmosphere_with_valid_pressure():
    # Normal operation.
    pressure_in_pascal = 123456
    reference = 1.2184
    output = pascal_to_atmosphere(pressure_in_pascal)
    msg = 'Reference "{}" does not match output "{}"'.format(reference, output)
    assert_almost_equal(output, reference, msg)


def test_pascal_to_atmosphere_with_zero_pressure():
    # Edge case.
    pressure_in_pascal = 0
    reference = 0
    output = pascal_to_atmosphere(pressure_in_pascal)
    msg = 'Reference "{}" does not match output "{}"'.format(reference, output)
    assert_almost_equal(output, reference, msg)
    

