"""This is the calculation class """
from app.addition import addition
from app.multiplication import multiplication
from app.division import division
from app.subtraction import subtraction


def test_addition_calculation():
    """Add Two Numbers"""
    addition_instance = Addition.create(2, 2)
    assert addition_instance.get_result() == 4, "Addition is not working"


class Calculation:
    """My Base Calculation Class"""
    result = 0

    @classmethod
    def create(cls, val1, val2):
        return cls(val1, val2)

    def get_result(self):
        """Get the result of a calculation"""
        return self.result

    def set_result(self, result):
        """Get the result of a calculation"""
        self.result = result


class Addition(Calculation):
    """My Addition Calculation Class"""

    def __init__(self, val1, val2):
        self.set_result(addition(val1, val2))


class Subtraction(Calculation):
    """My Subtraction Calculation Class"""

    def __init__(self, val1, val2):
        self.set_result(subtraction(val1, val2))


class Division(Calculation):
    """My Division Calculation Class"""

    def __init__(self, val1, val2):
        self.set_result(division(val1, val2))


class Multiplication(Calculation):
    """My Multiplication Calculation Class"""

    def __init__(self, val1, val2):
        self.set_result(multiplication(val1, val2))
