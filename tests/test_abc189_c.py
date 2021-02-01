# -*- coding: utf-8 -*-

from unittest import TestCase

import tests.utils as utils
from abc189.c.main import *

class Test_abc189_c(TestCase):

    def test_get_answer_1(self):
        list_A = [2, 4, 4, 9, 4, 9]

        self.assertEqual(20, get_answer(list_A))

    def test_get_answer_2(self):
        list_A = [1]
        self.assertEqual(1, get_answer(list_A))

    def test_get_answer_3(self):
        list_A = [100000]
        self.assertEqual(100000, get_answer(list_A))

    def test_get_answer_4(self):
        list_A = [a % 100000 for a in range(10000)]
        self.assertEqual(1, get_answer(list_A))

    def test_get_answer_5(self):
        list_A = [100000]
        self.assertEqual(100000, get_answer(list_A))
