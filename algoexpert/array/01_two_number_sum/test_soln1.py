import unittest

from .soln1 import two_number_sum


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
