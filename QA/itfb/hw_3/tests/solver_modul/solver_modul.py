from unittest import TestCase

from qa.itfb.hw_3.solver import Solver


class TestSolver(TestCase):

    def test_add(self):
        solver = Solver(2, 3)
        result = solver.add()
        self.assertEqual(result, 5)
