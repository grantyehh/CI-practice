import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        self.assertEqual(self.calc.sub(9, 5), 4)  # Expect 9 - 5 = 4

    def test_mult(self):
        self.assertEqual(self.calc.mul(3, 4), 12)  # Expect 3 x 4 = 12

    def test_div(self):
        result = self.calc.div(3, 2)
        self.assertIsInstance(result, float)  # check type
        self.assertEqual(result, 1.5)  # Expect 3 / 2 = 1.5
