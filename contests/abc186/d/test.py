# -*- coding: utf-8 -*-

from unittest import TestCase

from d.main import get_answer


class Test(TestCase):

    def test_fail(self):
        self.assertTrue(True)

    def test_get_ans1(self):
        N = 3
        L_A = [5, 1, 2]

        self.assertEqual(
            8,
            get_answer(N, L_A)
        )


