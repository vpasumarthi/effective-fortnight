"""
testing the math.py module.
"""

import effective_fortnight as ef
import pytest

def test_add():
    assert ef.math.add(3, 4) == 7
    assert ef.math.add(4, 4) == 8

testdata = [
    (2, 5, 10),
    (1, 2, 2),
    (3, 4, 12),
    (3, 3, 9),
    (6, 7, 42)
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert ef.math.mult(a, b) == expected
    assert ef.mult(b, a) == expected

def test_mod():
    assert ef.math.mod(4, 3) == 1
    assert ef.math.mod(6, 3) == 0

def test_power():
    assert ef.math.power(4, 2) == 16
    assert ef.power(2, 3) == 8

def test_min():
    assert ef.math.min(2, 3) == 2
    assert ef.math.min(3, 3) == 3

def test_max():
    assert ef.math.max(3, 4) == 4
    assert ef.math.max(4, 4) == 4
