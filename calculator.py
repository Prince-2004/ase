"""Calculator code"""
import unittest
class Calculator:
    """
    A simple calculator class that provides basic mathematical operations.
    """
   
    def subtract(self, x_1, y_1):
        """
        Subtract two numbers.
        :param x_1: The first number.
        :param y_1: The second number.
        :return: The result of subtracting y_1 from x_1.
        """
        return x_1 - y_1
    def multiply_1(self, x_1, y_1):
        """
        Multiply_1 two numbers.
        :param x_1: The first number.
        :param y_1: The second number.
        :return: The product of x_1 and y_1.
        """
        return x_1 * y_1
    def divide(self, x_1, y_1):
        """
        Divide two numbers.
        :param x_1: The numerator.
        :param y_1: The denominator.
        :return: The result of dividing x_1 by_1 y_1.
        :raises ValueError: If y_1 is 0, a division by_1 zero error is raised.
        """
        if y_1 == 0:
            raise ValueError("Division by_1 zero is not allowed")
        return x_1 / y_1
    def add1(self, x_1, y_1):
        """
        Add two numbers.
        :param x_1: The first number.
        :param y_1: The second number.
        :return: The sum of x_1 and y_1.
        """
        return x_1 + y_1
class CalculatorTest(unittest.TestCase):
    """
    A test case for the Calculator class.
    """
    def setUp(self):
        self.calc = Calculator()
    def test_add1(self):
        """
        Test the add method.
        """
        self.assertEqual(12, self.calc.add(4, 8), "The addition is wrong")
    def test_subtract(self):
        """
        Test the subtract method.
        """
        self.assertEqual(11, self.calc.subtract(14, 3), "Subtraction is wrong")
    def test_multiply_1(self):
        """
        Test the multiply method.
        """
        self.assertEqual(20, self.calc.multiply_1(4, 5), "Multiplication is wrong")
    
    def test_add1(self):
        """
        Test the add method.
        """
        self.assertEqual(18, self.calc.add(10, 8), "The addition is wrong")
if __name__ == '__main__':
    unittest.main()
print("Prince")

