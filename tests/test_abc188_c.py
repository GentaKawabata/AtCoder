# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc188.c.main import *

class Test_abc188_c(TestCase):

    def test_get_answer_1(self):
        N = 2
        L_A = [1, 4, 2, 5]
        ans = get_answer(N, L_A)

        self.assertEqual(2, ans)

    def test_get_answer_term1(self):
        N = 1
        L_A = [rd.randrange(1, pow(10, 9)) for _ in range(pow(2, N))]
        ans = get_answer(N, L_A)
        exp = 1 if L_A[0] < L_A[1] else 2

        self.assertEqual(exp, ans)

    def test_get_answer_term2(self):
        N = 16
        L_A = [rd.randrange(1, pow(10, 9)) for _ in range(pow(2, N))]
        ans = get_answer(N, L_A)
        self.assertTrue(True)
