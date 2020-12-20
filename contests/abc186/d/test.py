# -*- coding: utf-8 -*-

from unittest import TestCase

from contests.abc186.d.main import *


class Test(TestCase):

    def test_sort(self):
        L_A = [5, 1, 2]

        L_A.sort()

        self.assertEqual(
            [1, 2, 5],
            L_A
        )

    def test_get_ruiseki_wa_1(self):
        L_A = [1, 2, 5]

        exp = [0, 1, 3, 8]
        act = get_ruiseki_wa(L_A)

        self.assertEqual(exp, act)

    def test_get_ruiseki_wa_2(self):
        L_A = [-2, 0, 3, 9, 15, 26]

        exp = [0, -2, -2, 1, 10, 25, 51]
        act = get_ruiseki_wa(L_A)

        self.assertEqual(exp, act)

    def test_get_ruiseki_wa_3(self):
        L_A = [1, 6, 3, 8, 4, 2, 9, 5, 7]

        exp = [0, 1, 7, 10, 18, 22, 24, 33, 38, 45]
        act = get_ruiseki_wa(L_A)

        self.assertEqual(exp, act)
