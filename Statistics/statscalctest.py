import unittest
from Statistics import Statistics
## from Calculator.Calculator import Calculator
## from CsvReader import CsvReader
## from pprint import pprint
statistics = Statistics()

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(statistics, Statistics)

    def test_stat_mean_calc(self):
        data = [1,2,3,4,5]
        self.assertEqual(statistics.populationmean(data), 3)

    def test_stat_median_calc(self):
        data = [1, 2, 3, 4, 5, 6,7]
        self.assertEqual(statistics.popmedian(data), 4)

    def test_stat_mode_calc(self):
        data = [1,1,1,1,2,2,2, 3, 4, 5, 6, 7]
        self.assertEqual(statistics.popmode(data), 1)    

    def test_stat_popstd_calc(self):
        #data = [1,2,3,4,5,6]
        self.assertEqual(statistics.popstddev(), 1.707825)

    def test_stat_var_calc(self):
        val = [5,3,1,2,4]
        self.assertEqual(statistics.popvariance(val), 2)

if __name__ == '__main__':
    unittest.main()