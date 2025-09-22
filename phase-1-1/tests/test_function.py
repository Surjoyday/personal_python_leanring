# Import calculator functions to test
from app.calculator_function import add, subtract, multiply, divide
# Import pytest library for testing
import pytest

# Pytest is a popular Python testing framework.
# It helps automate the process of checking if your code works as expected.
# You write functions starting with 'test_' and pytest will find and run them.

def test_add():
    # 'assert' checks if the expression is True; if not, the test fails.
    assert add(2, 3) == 5  # Test if add returns correct sum
    assert add(-1, 1) == 0 # Test with negative and positive numbers
    assert add(0, 0) == 0  # Test with zeros

def test_subtract():
    assert subtract(5, 3) == 2  # Test subtraction
    assert subtract(0, 0) == 0  # Test with zeros
    assert subtract(-1, -1) == 0 # Test with negative numbers

def test_multiply():
    assert multiply(4, 5) == 20  # Test multiplication
    assert multiply(-1, 1) == -1 # Test with negative numbers
    assert multiply(0, 100) == 0 # Test multiplying by zero

def test_divide():
    assert divide(10, 2) == 5    # Test division
    assert divide(-6, 3) == -2   # Test with negative numbers

def test_divide_by_zero():
    # 'pytest.raises' checks if a specific error is raised.
    # Here, we expect ValueError when dividing by zero.
    with pytest.raises(ValueError):
        divide(5, 0)

# Why do we test?
# - To make sure our code works as expected (correctness).
# - To catch bugs early.
# - To make changes confidently (if tests pass, code is likely correct).

# What does pytest give us?
# - Finds and runs all test functions automatically.
# - Shows which tests passed or failed.
# - Lets us check for errors using 'pytest.raises'.
# - Easy to use with simple 'assert' statements.

# What does 'assert' do?
# - Checks if a condition is True.
# - If False, the test fails and pytest reports it.

# What does 'pytest.raises' do?
# - Checks if a block of code raises a specific error.
# - Useful for testing error handling (like divide by zero).

# How do you run tests?
# - Use 'poetry run pytest' in your terminal.
# - Poetry manages dependencies and runs pytest for you.
# - Pytest will find all files named 'test_*.py' and run the test functions.

# Summary:
# - Write test functions with 'test_' prefix.
# - Use 'assert' to check results.
# - Use 'pytest.raises' to check for errors.
# - Run tests with 'poetry run pytest'.
# - Pytest helps you write reliable, bug-free code.
