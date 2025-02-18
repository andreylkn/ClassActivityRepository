from week11.calculator.classes.simple_calculator import SimpleCalculator

class AdvanceCalculator(SimpleCalculator):
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def power(self, base, exponent):
        return base ** exponent
