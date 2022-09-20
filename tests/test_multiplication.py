"""This is the starting test file"""
from app.multiplication import multiplication


def test_multiplication():
    """This always passes"""
    product = multiplication(2, 2)
    assert product == 4
