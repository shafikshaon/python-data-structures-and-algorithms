import unittest

from .soln1 import non_constructible_coin


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        coins = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        output = non_constructible_coin(coins)
        self.assertEqual(output, expected)
