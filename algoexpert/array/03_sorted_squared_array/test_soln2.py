import unittest

from .soln2 import sorted_squared_array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = sorted_squared_array([1, 2, 3, 5, 6, 8, 9])
        self.assertEqual(output, [1, 4, 9, 25, 36, 64, 81])
