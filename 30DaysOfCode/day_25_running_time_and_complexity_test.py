#!/bin/python3

from day_25_running_time_and_complexity import PrimeNumber
import unittest

class PrimeNumberTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(False, PrimeNumber.is_prime(1))
        self.assertEqual(True, PrimeNumber.is_prime(5))
        self.assertEqual(True, PrimeNumber.is_prime(37))
        self.assertEqual(False, PrimeNumber.is_prime(66))

if __name__ == '__main__':
    unittest.main()
