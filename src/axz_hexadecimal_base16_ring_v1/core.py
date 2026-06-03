"""AXZ Hexadecimal Base-16 Ordered Ring V1 core verifier."""
from __future__ import annotations
from functools import lru_cache
from hashlib import sha256
from pathlib import Path

TOKENS = tuple(range(1, 10))
BASE = 16
TRUTH_LABEL = "CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES"
EXPECTED = {
    "possible_cut_patterns": 256,
    "unique_integer_values_generated": 179145,
    "positive_integer_values_generated": 95757,
    "nonpositive_integer_values_generated": 83388,
    "negative_integer_values_generated": 83387,
    "zero_present": True,
    "consecutive_positive_integers_from_1": 6007,
    "first_missing_positive_integer": 6008,
    "minimum_integer_value": -591751048,
    "maximum_integer_value": 4886718345,
    "all_interval_unique_values_generated": 187128,
    "all_values_sha256": "f10a798cb8395f57512fce2e497af6e6a41622f1aed06b38ef1c1f76d55d27fe",
    "positive_values_sha256": "f8d6d857f70d6c910f4674d8f764cc91c7a9d08d270cbecea83c7a2e30fe93d8",
    "nonpositive_values_sha256": "f35e613bab444d05a2bf22a64d28946d457fc7d30c750f517e9e2b7aac3f647c",
    "negative_values_sha256": "da826195aedbc8e41233c2bc6b4254c0579f661a6a35a5ae97b8165726e436fa",
    "all_interval_values_sha256": "499fb9b1599fe29734333510eee529da8967650664f006568b5852ab2f3c1710",
    "witness_table_sha256": "f999fb832234eed1b8eb824cd37bb67b050796ddd9549d93d0c276f1e125bbd2",
}

def concat_base16_interval(i: int, j: int, tokens: tuple[int, ...] = TOKENS) -> int:
    if not (0 <= i < j <= len(tokens)):
        raise ValueError("requires a nonempty valid token interval")
    value = 0
    for token in tokens[i:j]:
        if not (0 <= token < 16):
            raise ValueError("token is not a single hexadecimal digit")
        value = value * BASE + token
    return value

def hex_leaf(i: int, j: int, tokens: tuple[int, ...] = TOKENS) -> str:
    return "0x" + "".join(format(t, "X") for t in tokens[i:j])

@lru_cache(maxsize=None)
def values(i: int, j: int) -> frozenset[int]:
    out = {concat_base16_interval(i, j)}
    for k in range(i + 1, j):
        for a in values(i, k):
            for b in values(k, j):
                out.add(a + b)
                out.add(a - b)
                out.add(a * b)
    return frozenset(out)

@lru_cache(maxsize=None)
def witnesses(i: int, j: int) -> dict[int, str]:
    out = {concat_base16_interval(i, j): hex_leaf(i, j)}
    for k in range(i + 1, j):
        left = witnesses(i, k)
        right = witnesses(k, j)
        for a, ea in left.items():
            for b, eb in right.items():
                candidates = (
                    (a + b, f"({ea}+{eb})"),
                    (a - b, f"({ea}-{eb})"),
                    (a * b, f"({ea}*{eb})"),
                )
                for val, expr in candidates:
                    old = out.get(val)
                    if old is None or len(expr) < len(old) or (len(expr) == len(old) and expr < old):
                        out[val] = expr
    return out

def full_value_set() -> set[int]:
    return set(values(0, len(TOKENS)))

def all_interval_value_set() -> set[int]:
    out: set[int] = set()
    for i in range(len(TOKENS)):
        for j in range(i + 1, len(TOKENS) + 1):
            out.update(values(i, j))
    return out

def sha256_sorted_values(items) -> str:
    data = "".join(f"{x}\n" for x in sorted(items)).encode("utf-8")
    return sha256(data).hexdigest()

def consecutive_frontier(positive_values: set[int]) -> tuple[int, int]:
    target = 1
    for value in sorted(positive_values):
        if value == target:
            target += 1
        elif value > target:
            break
    return target - 1, target

def compute_certificate() -> dict[str, object]:
    full = full_value_set()
    positive = {x for x in full if x > 0}
    nonpositive = {x for x in full if x <= 0}
    negative = {x for x in full if x < 0}
    all_interval = all_interval_value_set()
    consecutive, missing = consecutive_frontier(positive)
    w = witnesses(0, len(TOKENS))
    return {
        "truth_label": TRUTH_LABEL,
        "tokens": list(TOKENS),
        "base": BASE,
        "possible_cut_patterns": 2 ** (len(TOKENS) - 1),
        "unique_integer_values_generated": len(full),
        "positive_integer_values_generated": len(positive),
        "nonpositive_integer_values_generated": len(nonpositive),
        "negative_integer_values_generated": len(negative),
        "zero_present": 0 in full,
        "consecutive_positive_integers_from_1": consecutive,
        "first_missing_positive_integer": missing,
        "minimum_integer_value": min(full),
        "maximum_integer_value": max(full),
        "all_interval_unique_values_generated": len(all_interval),
        "boundary_witness_expression": w[consecutive],
        "example_1551_representable": 1551 in full,
        "example_1551_expression": w.get(1551),
        "all_values_sha256": sha256_sorted_values(full),
        "positive_values_sha256": sha256_sorted_values(positive),
        "nonpositive_values_sha256": sha256_sorted_values(nonpositive),
        "negative_values_sha256": sha256_sorted_values(negative),
        "all_interval_values_sha256": sha256_sorted_values(all_interval),
    }

def read_sorted_int_file(path: str | Path) -> list[int]:
    text = Path(path).read_text(encoding="utf-8")
    return [int(line) for line in text.splitlines() if line.strip()]
