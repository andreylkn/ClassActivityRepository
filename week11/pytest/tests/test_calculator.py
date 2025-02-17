import pytest
from week11.pytest.mypackage.calculator_API import add, subtract, multiply, divide, factorial, power, is_prime

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_factorial():
    assert factorial(6) == 720

def test_power():
    assert power(2,6) == 64

def test_is_prime():
    assert is_prime(7)