from axz_hexadecimal_base16_ring_v1.core import EXPECTED, compute_certificate

def test_certificate_core_metrics():
    cert = compute_certificate()
    for key in [
        "unique_integer_values_generated",
        "positive_integer_values_generated",
        "nonpositive_integer_values_generated",
        "negative_integer_values_generated",
        "zero_present",
        "consecutive_positive_integers_from_1",
        "first_missing_positive_integer",
        "minimum_integer_value",
        "maximum_integer_value",
        "all_interval_unique_values_generated",
    ]:
        assert cert[key] == EXPECTED[key]

def test_claimed_old_wall_is_representable():
    cert = compute_certificate()
    assert cert["example_1551_representable"] is True
    assert cert["first_missing_positive_integer"] == 6008
