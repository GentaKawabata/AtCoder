# -*- coding: utf-8 -*-
from copy import copy


def get_answer_ij(l_a):
    if len(l_a) == 2:
        return abs(l_a[0] - l_a[1])
    else:
        total = 0
        for k in range(0, len(l_a)):
            total += abs(l_a[k] - l_a[-1])

        _ = l_a.pop(-1)
        return get_answer_ij(l_a) + total


def get_answer(n, l_a):
    return get_answer_ij(l_a)

# def get_answer_ij(l_a, j):
#     if j == 1:
#         return abs(l_a[0] - l_a[1])
#     else:
#         total = 0
#         for k in range(0, j):
#             total += abs(l_a[k] - l_a[j])
#
#         _ = l_a.pop(-1)
#         return get_answer_ij(l_a, j - 1) + total
#
#
# def get_answer(n, l_a):
#     return get_answer_ij(l_a, n - 1)
#

if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_A = list(map(int, input().split()))

    print(get_answer(N, L_A))
