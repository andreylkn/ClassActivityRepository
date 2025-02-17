import unittest
from week11.pytest.mypackage.calculator_API import add, subtract, multiply, divide, factorial, power, is_prime

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(4, 3), 1)
        self.assertEqual(subtract(-3, 1), -4)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(6, 3), 2)

    def test_factorial(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(6), 720)

    def test_pow(self):
        self.assertEqual(power(2, 6), 64)
        self.assertEqual(power(3, 5), 243)

    def test_is_prime(self):
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(31), True)
        self.assertEqual(is_prime(20), False)

if __name__ == '__main__':
    unittest.main()