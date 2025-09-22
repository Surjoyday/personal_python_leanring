import pytest
from app.calculator_oop import Calculator

@pytest.fixture
def calculator():
    return Calculator()


def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, -1) == 0
    assert calculator.subtract(-1, 1) == -2

def test_multiply(calculator):
    assert calculator.multiply(4, 5) == 20
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 100) == 0
    assert calculator.multiply(-2, -3) == 6

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(-6, -3) == 2
    assert calculator.divide(5, 2) == 2.5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

# This test file uses pytest to test the Calculator class methods.
# Each test function checks a specific method of the Calculator class.
# The 'calculator' fixture creates a new Calculator instance for each test.
# The tests cover normal cases and edge cases, including division by zero.  

# How to run tests?
# - Use 'poetry run pytest' in your terminal.