"""This is the calculation class """
from app.addition import addition
from app.multiplication import multiplication
from app.division import division
from app.subtraction import subtraction


def test_addition_calculation():
    """Add Two Numbers"""
    addition_instance = Addition.create(2, 2)
    assert addition_instance.get_result() == 4, "Addition is not working"


def test_addition_instance():
    """Add Two Numbers"""
    addition_instance = Addition.create(2, 2)
    assert isinstance(addition_instance, Addition), "Is not an Addition Instance If this Fails"


class Calculation:
    """My Base Calculation Class"""
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

    def get_result(self):
        """Get the result of a calculation"""
        return self.result


class Addition(Calculation):
    """My Addition Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor calls the """
        super().__init__(val1, val2)
        self.set_result(addition(self.val1, self.val2))


class Subtraction(Calculation):
    """My Subtraction Calculation Class"""

    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        self.set_result(subtraction(self.val1, self.val2))


class Division(Calculation):
    """My Division Calculation Class"""

    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        self.set_result(division(self.val1, self.val2))


class Multiplication(Calculation):
    """My Multiplication Calculation Class"""

    def __init__(self, val1, val2):
        super().__init__(val1, val2)
        self.set_result(multiplication(self.val1, self.val2))
