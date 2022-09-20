"""This is the starting test file"""
import pytest

from app.division import division


def test_division():
    """This always passes"""
    quotient = division(2, 2)
    assert quotient == 1


def test_division_div_zero():
    """This always passes"""
    with pytest.raises(ZeroDivisionError):
        quotient = division(2, 0)
