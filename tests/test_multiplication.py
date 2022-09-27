"""This is the starting test file"""
from app.multiplication import multiplication


def test_multiplication():
    """test multiplication"""
    assert multiplication(2, 2) == 4
