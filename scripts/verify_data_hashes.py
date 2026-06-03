from pathlib import Path
from hashlib import sha256
from axz_hexadecimal_base16_ring_v1.core import EXPECTED, sha256_sorted_values, read_sorted_int_file

ROOT = Path(__file__).resolve().parents[1]

def file_hash(path):
    return sha256(path.read_bytes()).hexdigest()

def main():
    checks = {
        "all_values_sha256": ROOT / "data" / "all_values_sorted.txt",
        "positive_values_sha256": ROOT / "data" / "positive_values_sorted.txt",
        "nonpositive_values_sha256": ROOT / "data" / "nonpositive_values_sorted.txt",
        "negative_values_sha256": ROOT / "data" / "negative_values_sorted.txt",
        "all_interval_values_sha256": ROOT / "data" / "all_interval_values_sorted.txt",
    }
    for key, path in checks.items():
        actual = sha256_sorted_values(read_sorted_int_file(path))
        assert actual == EXPECTED[key], f"{key} mismatch"
    witness_hash = file_hash(ROOT / "data" / "witnesses_1_to_6007.tsv")
    assert witness_hash == EXPECTED["witness_table_sha256"]
    print("PASS: DATA_HASHES_VERIFIED")

if __name__ == "__main__":
    main()
