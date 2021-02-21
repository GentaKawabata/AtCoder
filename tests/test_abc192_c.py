# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc192.c.main import *

class Test_abc192_c(TestCase):

    def test_get_answer_term_0(self):
        N, K = 0, 0
        self.assertEqual(0, get_answer(N, K))

    def test_get_answer_term_1(self):
        N, K = int(1e9), int(1e5)
        self.assertEqual(0, get_answer(N, K))

    def test_sample_1(self):
        N, K = 314, 2
        self.assertEqual(693, get_answer(N, K))

    def test_sample_2(self):
        N, K =1000000000, 100
        self.assertEqual(0, get_answer(N, K))

    def test_sample_3(self):
        N, K = 6174, 100000
        self.assertEqual(6174, get_answer(N, K))
