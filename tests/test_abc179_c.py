from unittest import TestCase

from abc179.c.main import *


class TestAbc179C_Kawa(TestCase):


    def test_get_answer_kawa_2(self):
        N = 2
        self.assertEqual(1, get_answer_kawa(N))

    def test_get_answer_kawa_3(self):
        N = 3
        self.assertEqual(3, get_answer_kawa(N))

    def test_get_answer_kawa_100(self):
        N = 100
        self.assertEqual(473, get_answer_kawa(N))

    def test_get_answer_kawa_1000000(self):
        N = 1000000
        self.assertEqual(13969985, get_answer_kawa(N))

class TestAbc179C_Example(TestCase):

    def test_get_answer_example_2(self):
        N = 2
        self.assertEqual(1, get_answer_example(N))

    def test_get_answer_example_3(self):
        N = 3
        self.assertEqual(3, get_answer_example(N))

    def test_get_answer_example_100(self):
        N = 100
        self.assertEqual(473, get_answer_example(N))

    def test_get_answer_example_1000000(self):
        N = 1000000
        self.assertEqual(13969985, get_answer_example(N))
