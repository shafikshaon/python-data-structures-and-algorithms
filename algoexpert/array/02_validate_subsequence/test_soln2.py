import unittest

from .soln2 import validate_subsequence


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
        self.assertTrue(output)
