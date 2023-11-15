def assert_almost_equal(value1, value2, msg):
    """
    Assert whether `value1` and `value2` are the same within a
    tolerance.

    The tolerance is equal to `0.0001`.

    Parameters
    ----------
    value1 : float
        The first value to be compared.
    value2 : float
        The second value to be compared.
    msg : string
        The message that will be printed (via the
        :class:`exceptions.AssertionError` exception) if `value1` and `value2`
        are not the same within the tolerance.
    """
    tolerance = 0.0001
    assert abs(value1 - value2) < tolerance, msg
