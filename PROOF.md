# Proof sketch

This certificate is finite. Let `V(i,j)` be the exact set of all integer values produced by the nonempty token interval from index `i` through `j-1`.

Base case: `V(i,j)` contains the Base-16 concatenation leaf for that interval.

Inductive step: for every split `i < k < j`, every `a in V(i,k)`, and every `b in V(k,j)`, the verifier inserts exactly:

```text
a + b
a - b
a * b
```

No commuted subtraction branch is inserted from the same split. This recurrence enumerates all allowed ordered binary expression trees and no forbidden trees.

The final universe is `V(0,9)`. The checked final universe contains every positive integer from `1` through `6007` and excludes `6008`. Therefore the first missing positive integer is `6008` under the stated rules.

Truth label: `CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES`.
