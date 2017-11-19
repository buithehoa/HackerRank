#!/bin/python3

import day_07_arrays
import unittest

class Arrays(unittest.TestCase):
    '''turn_me_upside_down should reverse the input array'''
    def test_reverse_array(self):
        arr = [ 1, 2, 3, 4 ]
        expected = [ 4, 3, 2, 1 ]

        result = day_07_arrays.turn_me_upside_down(arr)

        self.assertEqual(expected, result);

if __name__ == '__main__':
    unittest.main()
