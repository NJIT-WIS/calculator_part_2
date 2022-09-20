"""This is the starting test file"""
from app.addition import addition


def test_addition():
    """This always passes"""
    sum_num = addition(2, 2)
    assert sum_num == 4
