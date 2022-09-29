"""This is the calculation class """
import pytest

from app.calculations import Addition, Subtraction, Multiplication, Division


def test_addition_calculation():
    """Add Two Numbers"""
    # notice that each instance is independent of each other
    addition_instance_1 = Addition.create(2, 2)
    addition_instance_2 = Addition.create(3, 3)
    assert isinstance(addition_instance_1, Addition), "Is not a Addition Instance"
    assert isinstance(addition_instance_2, Addition), "Is not a Addition Instance"
    assert addition_instance_1.get_result() == 4, "Addition is not working"
    assert addition_instance_2.get_result() == 6, "Addition is not working"


def test_subtraction_calculation():
    """Subtract Two Numbers"""
    # notice that each instance is independent of each other
    subtraction_instance_1 = Subtraction.create(2, 2)
    subtraction_instance_2 = Subtraction.create(3, 2)
    assert isinstance(subtraction_instance_1, Subtraction), "Not a Subtraction Instance"
    assert isinstance(subtraction_instance_2, Subtraction), "Not a Subtraction Instance"
    assert subtraction_instance_1.get_result() == 0, "Subtraction is not working"
    assert subtraction_instance_2.get_result() == 1, "Subtraction is not working"


def test_multiplication_calculation():
    """Multiply Two Numbers"""
    # notice that each instance is independent of each other
    multiplication_instance_1 = Multiplication.create(2, 2)
    multiplication_instance_2 = Multiplication.create(3, 2)
    assert isinstance(multiplication_instance_1, Multiplication), "Not a Multiplication Instance"
    assert isinstance(multiplication_instance_2, Multiplication), "Not a Multiplication Instance"
    assert multiplication_instance_1.get_result() == 4, "Multiplication is not working"
    assert multiplication_instance_2.get_result() == 6, "Multiplication is not working"


def test_division_calculation():
    """Divide Two Numbers"""
    # notice that each instance is independent of each other
    division_instance_1 = Division.create(2, 2)
    division_instance_2 = Division.create(3, 2)

    assert isinstance(division_instance_1, Division), "Not a Multiplication Instance"
    assert isinstance(division_instance_1, Division), "Not a Multiplication Instance"
    assert division_instance_1.get_result() == 1, "Multiplication is not working"
    assert division_instance_2.get_result() == 1.5, "Multiplication is not working"
    with pytest.raises(ZeroDivisionError):
        division_instance_3 = Division.create(3, 0), "Fails Divide By Zero"
        del division_instance_3
