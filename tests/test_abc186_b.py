# -*- coding: utf-8 -*-

from unittest import TestCase

from abc186.b.main import *

class Test_abc186_b(TestCase):

    def test_get_answer_1(self):
        self.assertEqual("hoge", get_answer(3))
