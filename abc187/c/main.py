# -*- coding: utf-8 -*-

from typing import List


# def get_answer(n: int, l_s: List[str]):

#     for s in l_s:
#         if not "!" in s:
#             tmp = "!" + s
#             if tmp in l_s:
#                 return s
#     return "satisfiable"


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_S = []
    for _ in range(N):
        s = input()

        if "!" in s:
            replaced = s.replace("!", "")
            if replaced in L_S:
                print(replaced)
                quit()
        else:
            if "!" + s in L_S:
                print(s)
                quit()

        if not s in L_S:
            L_S.append(s)

    print("satisfiable")
