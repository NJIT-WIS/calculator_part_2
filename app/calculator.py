"""Calculator Class"""
from app.calculations import *


class Calculator:
    """Improved Calculator with Static Methods and using the calculation instance"""

    @staticmethod
    def add(val1, val2):
        return Addition.create(val1, val2).get_result()

    @staticmethod
    def divide(val1, val2):
        return Division.create(val1, val2).get_result()

    @staticmethod
    def multiply(val1, val2):
        return Multiplication.create(val1, val2).get_result()

    @staticmethod
    def subtract(val1, val2):
        return Subtraction.create(val1, val2).get_result()
