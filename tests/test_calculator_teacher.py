"""Do not change these tests, they are meant to check your code and should fail"""

from app.calculator import Calculator


def test_calculator_operations():
    """Basic Calculator Tests using the Instance"""
    assert Calculator.add(2, 2) == 4, "The Addition Function Failed"
    assert Calculator.divide(2, 2) == 1, "The Division Function Failed"
    assert Calculator.multiply(2, 2) == 4, "Multiplication Didn't work"
    assert Calculator.subtract(2, 2) == 0, "subtraction didn't work"
