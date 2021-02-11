# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils
from abc187.c.main import *

class Test_abc187_c(TestCase):

    def test_get_answer_1(self):
        N = 10
        L_S = [
            "red",
            "red",
            "red",
            "!orange",
            "yellow",
            "!blue",
            "cyan",
            "!green",
            "brown",
            "!gray"
        ]
        self.assertEqual("satisfiable", get_answer_list(N, L_S))

    def test_get_answer_2(self):
        N = 11
        L_S = [
            "red",
            "red",
            "red",
            "!orange",
            "yellow",
            "!blue",
            "cyan",
            "!green",
            "brown",
            "!gray",
            "!red"
        ]
        self.assertEqual("red", get_answer_list(N, L_S))

    def test_get_answer_term_list(self):

        N = 2 * pow(10, 5)
        S = []
        for _ in range(N):
            S.append("aaaaaaaaa")
        
        self.assertEqual("satisfiable", get_answer_list(N, S))

    def test_get_answer_term_set(self):

        N = 2 * pow(10, 5)
        S = []
        for _ in range(N):
            S.append("aaaaaaaaa")
        
        S = set(S)

        self.assertEqual("satisfiable", get_answer_set(N, S))