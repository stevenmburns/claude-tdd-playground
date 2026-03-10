import math
import timeit
from gcd import gcd, gcd_subtraction, gcd_modulo, gcd_binary_unscaled

CASES = [
    (12, 8),
    (48, 18),
    (100_000, 75_000),
    (1, 130_000_000),
]

IMPLEMENTATIONS = [
    ("subtraction", gcd_subtraction),
    ("binary    ", gcd),
    ("modulo    ", gcd_modulo),
    ("binary_us ", gcd_binary_unscaled),
    ("math.gcd  ", math.gcd),
]

REPEATS = 3

print(f"{'case':<30} {'impl':<14} {'time':>12}")
print("-" * 60)

for a, b in CASES:
    for label, fn in IMPLEMENTATIONS:
        t = timeit.timeit(lambda: fn(a, b), number=REPEATS) / REPEATS
        unit = "s" if t >= 0.001 else "µs"
        display = t if t >= 0.001 else t * 1_000_000
        print(f"gcd({a}, {b}){'':<{20 - len(str(a)) - len(str(b))}} {label}   {display:>10.3f} {unit}")
    print()
