import random
from unittest import TestCase

import utils as ut
from templates.search import *
from templates.dec_to_bin import *
from templates.combination import *
from templates.cumulative_sum import *


class TestBinarySearch(TestCase):

    def test_int_no_dupl(self):
        arr = [2, 5, 8, 9, 10]
        self.assertEqual(2, binary(8, arr))

    def test_int_with_dupl(self):
        arr = [2, 5, 8, 8, 9, 10]
        self.assertEqual(2, binary(8, arr))

    def test_str_no_dupl(self):
        arr = ["a", "k", "l", "p", "r", "w"]
        self.assertEqual(2, binary("l", arr))

    def test_str_with_dupl(self):
        arr = ["a", "k", "l", "p", "r", "r", "w"]
        self.assertEqual(4, binary("r", arr))

    def test_str_not_include(self):
        arr = ["a", "k", "l", "p", "r", "r", "w"]
        self.assertEqual(-1, binary("o", arr))
    
    def test_int_any(self):
        arr = [0, 0, 4, 5, 5, 7, 7, 7, 9, 9]
        self.assertEqual(0, binary(0, arr))

    def test_int_random(self):
        num_test = 10
        N = pow(10, 1)
        # N = 6
        rand_range = (0, 3)

        timer = ut.MyTimer()
        for i in range(num_test):
            print(f"### test {i}/{num_test} ###")
            key = random.randrange(rand_range[0], rand_range[1], 1)

            # timer.start()
            arr = [random.randrange(rand_range[0], rand_range[1], 1) for _ in range(N)]
            # print(f"time make arr = {timer.stop()}")

            # ソート
            # timer.start()
            arr.sort()
            # print(f"time sort = {timer.stop()}")

            # python 標準の index    
            py_index = -1
            time = -1
            if not key in arr:
                timer.start()
                py_index = -1
                time = timer.stop()
            else:
                timer.start()
                py_index = arr.index(key)
                time = timer.stop()
            print(f"time py index = {time}")

            # 逐次探索
            timer.start()
            seq_actual = sequential(key, arr)
            print(f"time seq = {timer.stop()}")
            print(f"(py_index, seq) = ({py_index}, {seq_actual})")
            with self.subTest(name=f"test seq {i}/{num_test}", key=key, arr=arr):
                self.assertEqual(py_index, seq_actual)

            # 二分探索
            timer.start()
            bin_actual = binary(key, arr)
            print(f"time bin = {timer.stop()}")
            print(f"(py_index, act) = ({py_index}, {bin_actual})")
            with self.subTest(name=f"test bin {i}/{num_test}", key=key, arr=arr):
                self.assertEqual(py_index, seq_actual)
                self.assertEqual(py_index, bin_actual)

            print("")


class TestDecToBin(TestCase):

    def test_3_3(self):
        # dec_to_bin(3, 3) -> [0, 1, 1]
        self.assertEqual([0, 1, 1], dec_to_bin(3, 3))

    def test_3_4(self):
        # dec_to_bin(3, 4) -> [0, 0, 1, 1]

        dec_no = 3
        a = dec_to_bin(dec_no, 4)


        self.assertEqual([0, 0, 1, 1], dec_to_bin(3, 4))


class TestCombination(TestCase):

    def test_11_1(self):
        n = 11
        m = 1
        self.assertEqual(11, combination(n, m))

    def test_11_11(self):
        n = 11
        m = 11
        self.assertEqual(1, combination(n, m))

    def test_199_11(self):
        n = 199
        m = 11
        self.assertEqual(366461620334848584, combination(n, m))


class TestCumulativeSum(TestCase):

    def test_get_cm_list_3(self):
        L_A = [1, 2, 3]
        cs_list = CumulativeSumList(L_A)
        self.assertEqual([0, 1, 3, 6], cs_list.cum_sum_list)

    def test_get_cm_list_5(self):
        L_A = [-1, -3, 1, -2, 3]
        cs_list = CumulativeSumList(L_A)
        self.assertEqual([0, -1, -4, -3, -5, -2], cs_list.cum_sum_list)

    def test_get_sum_3(self):
        L_A = [1, 2, 3]
        cs_list = CumulativeSumList(L_A)

        start = 0
        stop = 2
        self.assertEqual(3, cs_list.get_sum(start, stop))

