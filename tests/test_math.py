"""
testing the math.py module.
"""

import effective_fortnight as ef
import pytest

def test_add():
    assert ef.math.add(3, 4) == 7
    assert ef.math.add(4, 4) == 8

def test_mult():
    assert ef.math.mult(2, 5) == 10
    assert ef.mult(4, 3) == 12

def test_mod():
    assert ef.math.mod(4, 3) == 1
    assert ef.math.mod(6, 3) == 0

def test_power():
    assert ef.math.power(4, 2) == 16
    assert ef.power(2, 3) == 8

def test_min():
    assert ef.math.min(2, 3) == 2
    assert ef.math.min(3, 3) == 3

