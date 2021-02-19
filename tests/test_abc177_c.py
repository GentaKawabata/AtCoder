# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc177.c.main import *

class Test_abc177_c(TestCase):

    def test_get_answer_1(self):
        N = 2
        L_A = [1, 3]
        self.assertEqual(3, get_answer(N, L_A))

    def test_get_answer_2(self):
        N = int(2 * 1e5)
        L_A = [rd.randrange(int(1e8), int(1e9), 1) for _ in range(N)]
        ans = get_answer(N, L_A)
        self.assertTrue(True)

    def test_get_answer_3(self):
        N = 3
        L_A = [1, 2, 3]
        self.assertEqual(11, get_answer(N, L_A))




