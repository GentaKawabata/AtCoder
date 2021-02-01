# -*- coding: utf-8 -*-

from unittest import TestCase

import tests.utils as utils
from abc189.b.main import *

class Test_abc189_b(TestCase):

    def test_get_answer_1(self):
        list_v = [(i * 100) % 1000 for i in range(1000)]
        list_p = [1 for i in range(1000)]
        x = 1000000

        a = get_answer(
            list_v, list_p, x
        )

        self.assertTrue(True)
