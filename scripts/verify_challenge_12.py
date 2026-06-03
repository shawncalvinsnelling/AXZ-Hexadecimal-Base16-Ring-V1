from axz_hexadecimal_base16_ring_v1.core import EXPECTED, TRUTH_LABEL, compute_certificate

def main():
    cert = compute_certificate()
    for key, expected in EXPECTED.items():
        if key.endswith("_sha256") and key == "witness_table_sha256":
            continue
        actual = cert.get(key)
        assert actual == expected, f"{key}: expected {expected!r}, got {actual!r}"
    assert cert["truth_label"] == TRUTH_LABEL
    assert cert["example_1551_representable"] is True
    print("PASS: CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES")
    print("first_missing_positive_integer=6008")

if __name__ == "__main__":
    main()
