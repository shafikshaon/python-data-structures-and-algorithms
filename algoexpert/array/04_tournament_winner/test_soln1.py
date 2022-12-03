import unittest

from .soln1 import tournament_winner


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        output = tournament_winner(competitions, results)
        self.assertEqual(output, expected)
