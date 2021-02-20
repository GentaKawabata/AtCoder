# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc192.d.main import *

class Test_abc192_d(TestCase):

    def test_get_answer_sample_1(self):
        X = "22"
        M = 10
        self.assertEqual(2, get_answer(X, M))

    def test_get_answer_sample_2(self):
        X = "999"
        M = 1500
        self.assertEqual(3, get_answer(X, M))

    def test_get_answer_sample_3(self):
        X = "100000000000000000000000000000000000000000000000000000000000"
        M = 1000000000000000000
        self.assertEqual(1, get_answer(X, M))

    def test_get_answer_big_1(self):
        # temp = "1234567890"
        temp = "1000000000"
        X = temp
        for _ in range(6 - 1):
            # X += temp
            X += "0000000000"

        M = int(1e18)
        self.assertEqual(1, get_answer(X, M))

    def test_get_answer_min_1(self):
        X = "1"
        M = int(1e18)
        self.assertEqual(1, get_answer(X, M))
