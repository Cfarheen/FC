import unittest

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        result = calc.add(3, 5)
        self.assertEqual(result, 9)

    def test_subtraction(self):
        calc = Calculator()
        result = calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        calc = Calculator()
        result = calc.multiply(2, 7)
        self.assertEqual(result, 14)

    def test_division(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
