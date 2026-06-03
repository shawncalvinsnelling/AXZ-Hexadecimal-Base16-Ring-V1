def test_python_int_arbitrary_precision():
    guard = 2**130 + 123456789
    assert guard.bit_length() == 131
    assert guard + 1 > guard
