import unittest

from calculator import calculator
from csvreader import csvreader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_addition(self):
        test_data = csvreader('src/csv/UnitTestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)

    def test_subtraction(self):
        test_data = csvreader('src/csv/UnitTestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
