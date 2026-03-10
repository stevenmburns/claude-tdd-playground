import math
import time
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st
from gcd import gcd, gcd_subtraction, gcd_modulo, gcd_binary_unscaled


cases = [
    (12, 8, 4),
    (100, 75, 25),
    (17, 5, 1),
    (0, 5, 5),
    (7, 7, 7),
    (48, 18, 6),
    (16, 24, 8),   # gcd is a pure power of 2 (k=3)
    (24, 36, 12),  # gcd has a power-of-2 factor: 12 = 4 * 3 (k=2)
]


@pytest.mark.parametrize("a,b,expected", cases)
def test_gcd_matches_math(a, b, expected):
    assert gcd(a, b) == expected
    assert gcd(a, b) == math.gcd(a, b)


@pytest.mark.parametrize("a,b,expected", cases)
def test_gcd_modulo(a, b, expected):
    assert gcd_modulo(a, b) == expected
    assert gcd_modulo(a, b) == math.gcd(a, b)


@pytest.mark.parametrize("a,b,expected", cases)
def test_gcd_binary_unscaled(a, b, expected):
    assert gcd_binary_unscaled(a, b) == expected
    assert gcd_binary_unscaled(a, b) == math.gcd(a, b)


nonneg = st.integers(min_value=0, max_value=10_000_000)


@pytest.mark.hypothesis
@given(a=nonneg, b=nonneg)
@settings(max_examples=500)
def test_property_gcd_matches_math(a, b):
    assert gcd(a, b) == math.gcd(a, b)


@pytest.mark.hypothesis
@given(a=nonneg, b=nonneg)
@settings(max_examples=500)
def test_property_gcd_modulo_matches_math(a, b):
    assert gcd_modulo(a, b) == math.gcd(a, b)


@pytest.mark.hypothesis
@given(a=nonneg, b=nonneg)
@settings(max_examples=500)
def test_property_gcd_binary_unscaled_matches_math(a, b):
    assert gcd_binary_unscaled(a, b) == math.gcd(a, b)


@pytest.mark.slow
def test_modulo_vs_subtraction_slow_case():
    """gcd(1, 130_000_000) takes ~10s on subtraction, <1ms on modulo."""
    N = 130_000_000

    start = time.perf_counter()
    result = gcd_modulo(1, N)
    elapsed_modulo = time.perf_counter() - start

    assert result == 1
    assert elapsed_modulo < 0.01, f"modulo should be fast, got {elapsed_modulo:.4f}s"


@pytest.mark.slow
def test_subtraction_slow_case():
    """gcd(1, 130_000_000) takes ~10s on the subtraction impl, <1ms on binary."""
    N = 130_000_000

    start = time.perf_counter()
    result = gcd_subtraction(1, N)
    elapsed = time.perf_counter() - start

    assert result == 1
    assert elapsed > 5, f"expected ~10s, got {elapsed:.1f}s — algorithm may have changed"
