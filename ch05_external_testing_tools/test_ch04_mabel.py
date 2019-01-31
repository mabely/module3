import pytest

import unittest
from ch04_mabel import is_prime

class Prime_test(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))
    def test_is_eight_prime(self):
        self.assertFalse(is_prime(8), msg='8 is not prime')
    def test_is_deci_prime(self):
        self.assertFalse(is_prime(5.3), msg='decimals not prime')
    def test_is_one_prime(self):
        self.assertFalse(is_prime(1))
    def test_is_neg_prime(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))
    def test_is_str_prime(self):
        with self.assertRaises(TypeError):
            is_prime('one')

if __name__ == '__main__':
    unittest.main()
