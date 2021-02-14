# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc185.c.main import *

class Test_abc185_c(TestCase):

    def test_get_answer_200(self):
        L = 200
        self.assertEqual(366461620334848584, get_answer(L))

    def test_get_answer_12(self):
        L = 12
        self.assertEqual(1, get_answer(L))

    def test_get_answer_14(self):
        L = 14
        self.assertEqual(78, get_answer(L))

    def test_get_answer_20(self):
        L = 20
        self.assertEqual(75582, get_answer(L))
