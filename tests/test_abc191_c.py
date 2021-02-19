# -*- coding: utf-8 -*-

from unittest import TestCase

# import tests.utils as utils
# import utils
from abc191.c.main import *


class Test_abc191_c(TestCase):

    # def test_count_balack_1(self):
    #     l_s = ".###."
    #     self.assertEqual(3, count_black(l_s))

    def test_get_answer_1(self):
        H = 5
        W = 5
        S = [
            ".....",
            ".###.",
            ".###.",
            ".###.",
            "....."
        ]

        self.assertEqual(4, get_answer(H, W, S))

    def test_get_answer_2(self):
        H = 5
        W = 5
        S = [
            ".....",
            ".#...",
            ".##..",
            ".###.",
            "....."
        ]

        self.assertEqual(8, get_answer(H, W, S))

    def test_get_answer_3(self):
        H = 5
        W = 7
        S = [
            ".......",
            "..##...",
            ".####..",
            ".####..",
            "......."
        ]

        self.assertEqual(8, get_answer(H, W, S))

    def test_get_answer_4(self):
        H = 9
        W = 13
        S = [
            ".............",
            "...######....",
            "..########...",
            ".##########..",
            ".#########...",
            "..#######....",
            "...#####.....",
            "....###......",
            "............."
        ]

        self.assertEqual(26, get_answer(H, W, S))

    def test_get_answer_5(self):
        H = 3
        W = 3
        S = [
            "...",
            ".#.",
            "..."
        ]

        self.assertEqual(4, get_answer(H, W, S))


    def test_get_answer_6(self):
        H = 10
        W = 10
        S = [
            "..........",
            ".#####....",
            ".####.....",
            ".###......",
            ".####.....",
            ".#####....",
            ".######...",
            ".#######..",
            ".########.",
            ".........."
        ]

        self.assertEqual(18, get_answer(H, W, S))
