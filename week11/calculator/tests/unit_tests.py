import unittest

from week11.calculator.classes.advance_calculator import AdvanceCalculator
from week11.calculator.classes.simple_calculator import SimpleCalculator

class TestMathOperationsOfSimpleCalculator(unittest.TestCase):
    def test_add(self):
        c = SimpleCalculator()
        self.assertEqual(c.add(2, 3), 5)
        self.assertEqual(c.add(-1, 1), 0)

    def test_subtract(self):
        c = SimpleCalculator()
        self.assertEqual(c.subtract(4, 3), 1)
        self.assertEqual(c.subtract(-3, 1), -4)

    def test_multiply(self):
        c = SimpleCalculator()
        self.assertEqual(c.multiply(2, 4), 8)
        self.assertEqual(c.multiply(3, 2), 6)

    def test_divide(self):
        c = SimpleCalculator()
        self.assertEqual(c.divide(8, 2), 4)
        self.assertEqual(c.divide(6, 3), 2)

class TestMathOperationsOfAdvanceCalculator(unittest.TestCase):
    def test_factorial(self):
        c = AdvanceCalculator()
        self.assertEqual(c.factorial(2), 2)
        self.assertEqual(c.factorial(4), 24)
        self.assertEqual(c.factorial(6), 720)

    def test_pow(self):
        c = AdvanceCalculator()
        self.assertEqual(c.power(2, 6), 64)
        self.assertEqual(c.power(3, 5), 243)

    def test_is_prime(self):
        c = AdvanceCalculator()
        self.assertEqual(c.is_prime(3), True)
        self.assertEqual(c.is_prime(31), True)
        self.assertEqual(c.is_prime(20), False)

if __name__ == '__main__':
    unittest.main()