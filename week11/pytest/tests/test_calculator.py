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

@pytest.mark.parametrize("value, expected_result", [
    (2, 2),
    (4, 24),
    (6, 720),
])
def test_factorial(value, expected_result):
    assert factorial(value) == expected_result

@pytest.mark.parametrize("base, exponent, expected_result", [
    (2, 6, 64),
    (3, 5, 243),
])
def test_power(base, exponent, expected_result):
    assert power(base,exponent) == expected_result

@pytest.mark.parametrize("value, expected_result", [
    (3, True),
    (31, True),
    (20, False)
])
def test_is_prime(value, expected_result):
    assert is_prime(value) == expected_result