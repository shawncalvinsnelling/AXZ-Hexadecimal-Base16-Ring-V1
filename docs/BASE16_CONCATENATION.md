# Base-16 concatenation

Base-16 concatenation is positional fusion in hexadecimal notation. Concatenating `1` and `2` produces `0x12`, equal to decimal 18. Concatenating `1`, `2`, and `3` produces `0x123`, equal to decimal 291.

For adjacent blocks `A` and `B`:

```text
Concat_16(A, B) = (A * 16^len_hex(B)) + B
```

In this repository, the input tokens are the one-digit hexadecimal tokens `1` through `9`.
