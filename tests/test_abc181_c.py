# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc181.c.main import *

class Test_abc181_c(TestCase):

    def test_get_answer_big(self):
        N = 100

        L_XY = [[rd.randrange(-1000, 1000, 1), rd.randrange(-1000, 1000, 1)] for _ in range(N)]

        print(get_answer(N, L_XY))

        self.assertTrue(True)
