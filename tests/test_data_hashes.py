from pathlib import Path
from hashlib import sha256
from axz_hexadecimal_base16_ring_v1.core import EXPECTED, read_sorted_int_file, sha256_sorted_values

ROOT = Path(__file__).resolve().parents[1]

def test_value_hashes():
    for key, name in {
        "all_values_sha256": "all_values_sorted.txt",
        "positive_values_sha256": "positive_values_sorted.txt",
        "nonpositive_values_sha256": "nonpositive_values_sorted.txt",
        "negative_values_sha256": "negative_values_sorted.txt",
        "all_interval_values_sha256": "all_interval_values_sorted.txt",
    }.items():
        assert sha256_sorted_values(read_sorted_int_file(ROOT / "data" / name)) == EXPECTED[key]

def test_witness_table_hash():
    data = (ROOT / "data" / "witnesses_1_to_6007.tsv").read_bytes()
    assert sha256(data).hexdigest() == EXPECTED["witness_table_sha256"]
