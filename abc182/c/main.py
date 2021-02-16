# -*- coding: utf-8 -*-

from typing import List
import itertools


def get_answer(str_n: str) -> int:

    k = len(str_n)
    l_index = [i for i in range(k)]
    l_str_n = list(str_n)

    num_pickup = k
    while num_pickup > 0:
        list_kumiawase = itertools.combinations(l_index, num_pickup)

        for kumiawase in list_kumiawase:
            kumiawase = list(kumiawase)
            l_str_number = []
            for index in kumiawase:
                l_str_number.append(l_str_n[index])

            if int("".join(l_str_number)) % 3 == 0:
                return k - num_pickup

        num_pickup -= 1
    
    return -1


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())
    pass

    N = input()
    print(get_answer(N))

