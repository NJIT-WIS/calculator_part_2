"""Calculator Class"""

from app.operations import addition
from app.operations import division
from app.operations import multiplication
from app.operations import subtraction


class Calculator:
    """Basic Calculator with Static Methods"""

    @staticmethod
    def add(val1, val2):
        return addition(val1, val2)

    @staticmethod
    def divide(val1, val2):
        return division(val1, val2)

    @staticmethod
    def multiply(val1, val2):
        return multiplication(val1, val2)

    @staticmethod
    def subtract(val1, val2):
        return subtraction(val1, val2)
