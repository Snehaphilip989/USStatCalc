import unittest
from Calculator import Calculator
## from CsvReader import CsvReader
## from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_stat_mean_calc(self):
        data = [1,2,3,4,5]
        self.assertEqual(self.calculator.populationmean(data), 3)

    def test_stat_median_calc(self):
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.calculator.popmedian(data), 3.5)


if __name__ == '__main__':
    unittest.main()