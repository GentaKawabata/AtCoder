# -*- coding: utf-8 -*-

from unittest import TestCase

# import tests.utils as utils
# import utils
from abc190.c.main import *

class Test_abc190_c(TestCase):

    def test_get_answer_1(self):
        N = 4
        M = 4
        L_A = [1, 1, 2, 3]
        L_B = [2, 3, 4, 4]
        K = 3
        L_C = [1, 1, 2]
        L_D = [2, 3, 3]

        self.assertEqual(2, get_answer(N, M, K, L_A, L_B, L_C, L_D))

    def test_get_answer_1(self):
        import random
        N = 100
        M = 100
        L_A = [random.randrange(1, N) for _ in range(M)]
        L_B = [random.randrange(1, N) for _ in range(M)]
        K = 16
        L_C = [random.randrange(1, N) for _ in range(K)]
        L_D = [random.randrange(1, N) for _ in range(K)]

        self.assertTrue(True)

    def test_dec_to_bin_7(self):
        result = dec_to_bin(7, 3)
        self.assertEqual([1, 1, 1], result)

    def test_dec_to_bin_3(self):
        result = dec_to_bin(3, 3)
        self.assertEqual([0, 1, 1], result)

    def test_dec_to_bin_6(self):
        result = dec_to_bin(6, 3)
        self.assertEqual([1, 1, 0], result)



