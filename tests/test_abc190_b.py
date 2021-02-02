# -*- coding: utf-8 -*-

from unittest import TestCase

# import tests.utils as utils
# import utils
from abc190.b.main import *

class Test_abc190_b(TestCase):

    def test_get_answer_1(self):
        N = 100
        S = pow(10, 9)
        D = pow(10, 9)

        import random

        L_X = [random.randrange(1, pow(10, 9)) for _ in range(100)]
        L_Y = [random.randrange(1, pow(10, 9)) for _ in range(100)]

        print(get_answer(N, S, D, L_X, L_Y))

        self.assertTrue(True)
