# -*- coding: utf-8 -*-
from copy import copy


def get_ruiseki_wa(in_list):
    if len(in_list) == 0:
        return [0]
    else:
        tail = in_list.pop(-1)
        ruiseki_list = get_ruiseki_wa(in_list)

        tail_of_pre = ruiseki_list[-1]
        return ruiseki_list + [tail_of_pre + tail]


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
    l_a.sort()

    return get_answer_ij(l_a)


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
