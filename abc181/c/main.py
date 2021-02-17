# -*- coding: utf-8 -*-


from typing import List

import itertools
import math


def len_btw_points(p1, p2):
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


# def area_tri(len_edge1, len_edge2, len_edge3):
#     d = (len_edge1 + len_edge2 + len_edge3) / 2.0
#     return math.sqrt(d * (d - len_edge1) * (d- len_edge2) * (d - len_edge3))


def get_answer(n: int, l_xy: List[List[int]]):

    l_index = [i for i in range(n)]
    all_comb = list(itertools.combinations(l_index, 3))

    for comb in all_comb:
        len_edge1 = len_btw_points(l_xy[comb[0]], l_xy[comb[1]])
        len_edge2 = len_btw_points(l_xy[comb[0]], l_xy[comb[2]])
        len_edge3 = len_btw_points(l_xy[comb[1]], l_xy[comb[2]])

        if len_edge1 >= len_edge2 + len_edge3:
            return "Yes"
        if len_edge2 >= len_edge1 + len_edge3:
            return "Yes"
        if len_edge3 >= len_edge1 + len_edge2:
            return "Yes"

    return "No"


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_XY = []
    for _ in range(N):
        L_XY.append(list(map(int, input().split())))

    print(get_answer(N, L_XY))
