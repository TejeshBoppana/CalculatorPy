import unittest

from calculator import calculator
from csvreader import csvreader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_addition(self):
        test_data = csvreader('../src/csv/UnitTestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)

    def test_subtraction(self):
        test_data = csvreader('../src/csv/UnitTestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_times(self):
        test_data = csvreader('../src/csv/UnitTestMultiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_div(self):
        test_data = csvreader('../src/csv/UnitTestDivision.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.division(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square(self):
        test_data = csvreader('../src/csv/UnitTestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square_(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        test_data = csvreader('../src/csv/UnitTestSquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sqrt_(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)
