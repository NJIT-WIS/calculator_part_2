"""This is the starting test file"""
from app.subtraction import subtraction


def test_subtraction():
    """This always passes"""
    difference = subtraction(2, 2)
    assert difference == 0