import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4, 2), 6)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(5,2), 3)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(4, 2), 8)
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(9, 3), 3)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,5), 0)
        self.assertEqual(self.calc.modulo(9,4), 1)

if __name__ == '__main__':
    unittest.main()