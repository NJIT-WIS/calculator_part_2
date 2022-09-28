"""This is the calculation class """
from app.operations import *


def test_addition_calculation():
    """Add Two Numbers"""
    # notice that each instance is independent of each other
    addition_instance_1 = Addition.create(2, 2)
    addition_instance_2 = Addition.create(3, 3)

    assert addition_instance_1.get_result() == 4, "Addition is not working"
    assert addition_instance_2.get_result() == 6, "Addition is not working"


def test_addition_instance():
    """Add Two Numbers"""
    addition_instance = Addition.create(2, 2)
    assert isinstance(addition_instance, Addition), "Is not an Addition Instance If this Fails"


class Calculation:
    """My abstract Base Calculation Class"""
    result = 0
    val1 = 0
    val2 = 0

    @classmethod
    def create(cls, val1, val2):
        """Factory Method"""
        return cls(val1, val2)

    def __init__(self, val1, val2):
        """This is the base class constructor"""
        self.val1 = val1
        self.val2 = val2

    def set_result(self, result):
        """Get the result of a calculation"""
        self.result = result

    def set_val1(self, val1):
        """Get the result of a calculation"""
        self.val1 = val1

    def set_val2(self, val2):
        """Get the result of a calculation"""
        self.val2 = val2

    def get_val1(self):
        """Get the result of a calculation"""
        return self.val1

    def get_val2(self):
        """Get the result of a calculation"""
        return self.val2

    def get_result(self):
        """Get the result of a calculation"""
        return self.result


class Addition(Calculation):
    """My Addition Concrete Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor calls the """
        super().__init__(val1, val2)
        self.set_result(addition(self.val1, self.val2))


class Subtraction(Calculation):
    """My Subtraction Concrete Calculation Class"""

    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        self.set_result(subtraction(self.val1, self.val2))


class Division(Calculation):
    """My Division Concrete Calculation Class"""

    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        self.set_result(division(self.val1, self.val2))


class Multiplication(Calculation):
    """My Multiplication Concrete Calculation Class"""

    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        self.set_result(multiplication(self.val1, self.val2))
