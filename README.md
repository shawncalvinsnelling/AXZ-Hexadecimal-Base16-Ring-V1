# AXZ Hexadecimal Base-16 Ordered Ring V1

This repository is a finite exact computational certificate for the ordered hexadecimal token sequence:

```text
1 2 3 4 5 6 7 8 9
```

The project studies fixed-order single-hex-digit tokens under Base-16 concatenation, `+`, `-`, and `*`, with all ordered binary expression trees. All results are expressed as standard base-10 integers.

## Core definition

Each token is a one-digit hexadecimal block. Concatenating adjacent tokens uses Base-16 positional fusion:

```text
Concat_16(A, B) = (A * 16^len_hex(B)) + B
```

For this repository every input token is a single hexadecimal digit, so merging `1` and `2` produces `0x12`, which equals `18` in base 10. Merging `1`, `2`, and `3` produces `0x123`, which equals `291` in base 10.

For every interval of tokens, the dynamic program starts with the Base-16 concatenation leaf and then combines every valid left/right split by:

```text
A + B
A - B
A * B
```

Subtraction is **directional**: only left subtree minus right subtree is generated from a split. The evaluator does not add the swapped branch `B - A` unless it appears through a different valid syntactic parse.

## Certified finite result

Under the stated rules, every positive integer from `1` through `6,007` is representable, and the first missing positive integer is:

```text
6008
```

Important correction: the draft value `1551` is representable in this exact universe. The certificate records the witness:

```text
1551 = ((((0x1*0x23)-0x4)+0x567)+0x89)
```

## Certificate metrics

| Metric | Value |
|---|---:|
| Input tokens | `1 2 3 4 5 6 7 8 9` |
| Base | 16 |
| Possible cut patterns | 256 |
| Unique integer values generated | 179,145 |
| Positive integer values generated | 95,757 |
| Non-positive integer values generated | 83,388 |
| Negative integer values generated | 83,387 |
| Zero present | true |
| Consecutive positive integers from 1 | 6,007 |
| First missing positive integer | 6,008 |
| Minimum integer value | -591,751,048 |
| Maximum integer value | 4,886,718,345 |
| All-interval unique values generated | 187,128 |

## Boundary witness

```text
6007 = ((((0x12+0x345)-0x67)*0x8)-0x9)
```

The verifier checks that `6008` is absent from the exact dynamic-programming value set.

## Hashes

```text
All-values SHA-256:
f10a798cb8395f57512fce2e497af6e6a41622f1aed06b38ef1c1f76d55d27fe

Positive-values SHA-256:
f8d6d857f70d6c910f4674d8f764cc91c7a9d08d270cbecea83c7a2e30fe93d8

Non-positive-values SHA-256:
f35e613bab444d05a2bf22a64d28946d457fc7d30c750f517e9e2b7aac3f647c

Negative-values SHA-256:
da826195aedbc8e41233c2bc6b4254c0579f661a6a35a5ae97b8165726e436fa

All-interval-values SHA-256:
499fb9b1599fe29734333510eee529da8967650664f006568b5852ab2f3c1710

Witness table SHA-256:
f999fb832234eed1b8eb824cd37bb67b050796ddd9549d93d0c276f1e125bbd2
```

## Truth label

```text
CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES
```

This repository proves only this finite Base-16 ordered-expression universe under the exact stated rules. It does not claim to solve any famous open problem, universal multi-base digit-expression field, or asymptotic theorem.

## Reproduce locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
export PYTHONPATH="$PWD/src"      # Windows PowerShell: $env:PYTHONPATH="$PWD/src"

python scripts/verify_runtime_safety.py
python scripts/verify_challenge_12.py
python scripts/verify_data_hashes.py
python -m pytest -q
```

Expected result:

```text
PASS: ARBITRARY_PRECISION_RUNTIME_GUARD
PASS: CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES
PASS: DATA_HASHES_VERIFIED
```

## Safe public wording

```text
This project publishes a reproducible finite certificate for the Base-16 ordered token sequence 1 through 9 under fixed order, Base-16 concatenation, +, -, ×, and directional subtraction.
```
