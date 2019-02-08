"""
Test reduce function
"""

import unittest

from reduce import reduce


class ReduceTestCase(unittest.TestCase):
    def test_empty_array(self):
        result, step = reduce([])
        self.assertIsNone(result)
        self.assertIsNone(step)

    def test_single_element(self):
        result, step = reduce([1])
        self.assertEqual(result, 1)
        self.assertEqual(step, 0)

    def test_two_elements(self):
        result, step = reduce([1, 2])
        self.assertEqual(result, 3)
        self.assertEqual(step, 1)

    def test_odd_elements(self):
        test_array = [33, 6, 9, 1, 23, 88, 2]
        result, step = reduce(test_array)
        self.assertEqual(result, 162)
        self.assertEqual(step, 3)

    def test_even_elements(self):
        test_array = [33, 6, 9, 1, 23, 88, 2, 123]
        result, step = reduce(test_array)
        self.assertEqual(result, 285)
        self.assertEqual(step, 3)


if __name__ == '__main__':
    unittest.main()
