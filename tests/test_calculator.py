"""This is the starting test file"""
from app.multiplication import multiplication


def test_calculator_instance():
    """This always passes"""
    product = basic_calculator.multiply(2, 2)
    assert product == 4


class basic_calculator():
    @staticmethod
    def multiply_static(val1, val2):
        return multiplication(val1, val2)

    def multiply_instance(self, val1, val2):
        return multiplication(val1, val2)

    def multiply_class(cls, val1, val2):
        return multiplication(val1, val2)

