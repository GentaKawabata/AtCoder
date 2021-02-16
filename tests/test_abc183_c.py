# -*- coding: utf-8 -*-

from unittest import TestCase

# import tests.utils as utils
# import utils
from abc183.c.main import *

class Test_abc183_c(TestCase):

    def test_get_answer_1(self):
        N = 4
        K = 330
        T = [
            [0, 1, 10, 100],
            [1, 0, 20, 200],
            [10, 20, 0, 300],
            [100, 200, 300, 0]
        ]
        self.assertEqual(2, get_answer(N, K, T))

    def test_get_answer_2(self):
        N = 5
        K = 5
        T = [
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ]
        self.assertEqual(24, get_answer(N, K, T))

    def test_get_answer_3(self):
        N = 8
        K = pow(10, 9)
        T = [[pow(10, 8) for _ in range(N)] for _ in range(N)]

        self.assertTrue(True)
