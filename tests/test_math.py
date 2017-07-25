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
