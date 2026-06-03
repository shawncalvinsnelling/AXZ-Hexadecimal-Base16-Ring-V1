from pathlib import Path
from axz_hexadecimal_base16_ring_v1.core import EXPECTED, full_value_set

ROOT = Path(__file__).resolve().parents[1]

def test_witness_table_covers_frontier():
    lines = (ROOT / "data" / "witnesses_1_to_6007.tsv").read_text(encoding="utf-8").splitlines()
    assert lines[0] == "n\texpression"
    assert len(lines) == EXPECTED["consecutive_positive_integers_from_1"] + 1
    assert lines[-1].startswith("6007\t")

def test_first_missing_absent_and_boundary_present():
    full = full_value_set()
    assert 6007 in full
    assert 6008 not in full
