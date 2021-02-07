# -*- coding: utf-8 -*-

from unittest import TestCase

# import tests.utils as utils
# import utils
from abc191.b.main import *

class Test_abc191_b(TestCase):

    def test_get_answer_1(self):
        N = 5
        X = 5
        A = [3, 5, 6, 5, 4]

        self.assertEqual("3 6 4", get_answer(N, X, A))


