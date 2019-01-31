import unittest
from ch05_mabel import Calculator

class calc_tdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_calc_add_result_check(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)
    def test_calc_add_deci(self):
        result = self.calc.add(2.3,7.7)
        self.assertEqual(result, 10)
    def test_calc_add_str(self):
        result = self.calc.add('hello', 'world')
        with self.assertRaises(ValueError, result):
            pass

if __name__ == '__main__':
    unittest.main()
