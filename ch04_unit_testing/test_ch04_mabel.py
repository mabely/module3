import unittest
from ch04_mabel import is_prime

class prime_test(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5.3))

if __name__ == '__main__':
    unittest.main()
