from templates.dec_to_bin import dec_to_bin
from unittest import TestCase

from templates.dec_to_bin import *


class TestDecToBin(TestCase):

    def test_3_3(self):
        # dec_to_bin(3, 3) -> [0, 1, 1]
        self.assertEqual([0, 1, 1], dec_to_bin(3, 3))

    def test_3_4(self):
        # dec_to_bin(3, 4) -> [0, 0, 1, 1]

        dec_no = 3
        a = dec_to_bin(dec_no, 4)


        self.assertEqual([0, 0, 1, 1], dec_to_bin(3, 4))
