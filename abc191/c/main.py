# -*- coding: utf-8 -*-

from typing import List

def count_around_white_seq(i, j, S):
    # 連続するwhiteの最大数

    n = 2   # 2周しよう

    max_count = 0
    count = 0

    for _ in range(2):

        if S[i-1][j-1] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

        if S[i-1][j] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

        if S[i-1][j+1] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

        if S[i][j+1] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

        if S[i+1][j+1] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

        if S[i+1][j] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0


        if S[i+1][j-1] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

        if S[i][j-1] == ".":
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

    if max_count >= 8:
        max_count = 8

    return max_count


# def count_black(line_s):

#     ans = 0
#     for sij in line_s:
#         if sij == "#":
#             ans += 1
    
#     return ans


def get_answer(H, W, S: List[str]):
    # 周りの白の数が4つ以上で角と判定

    ans = 0

    for i, si in enumerate(S):

        if i == 0 or i == H - 1:
            continue
        for j, sij in enumerate(si):
            if j == 0 or j == W - 1 or sij == ".":
                continue

            n_around_white = count_around_white_seq(i, j, S)
            if n_around_white in [2, 4, 5, 6, 7, 8]:
                ans += 1

    if ans == 1 or ans == 2:
        ans = 4

    return ans



if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())
    pass


    _H, _W = map(int, input().split())

    _S = []
    for _ in range(_H):
        _S.append(input())

    print(get_answer(_H, _W, _S))
