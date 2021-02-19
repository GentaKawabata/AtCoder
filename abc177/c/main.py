# -*- coding: utf-8 -*-

from typing import List

MOD = int(1e9 + 7)

def get_cumulative_sum_sequential_mod(numbers: List[int]):
    """forで累積和を求める。 MOD 使用
    This method works.
    """
    result: List[int] = [0]

    for number in numbers:
        sum = result[-1] + number
        if sum < 0:
            sum += MOD
        sum %= MOD
        result.append(sum)
    return result

def get_sum(l_c, start, stop):
    """
    元の配列 L_A の A_start + ... + A_{stop-1} を求める
    """
    return l_c[stop] - l_c[start]

def get_answer(n, l_a):

    l_c = get_cumulative_sum_sequential_mod(l_a)
    result = 0
    for i in range(n - 1):
        a = l_a[i]
        b = get_sum(l_c, i + 1, n)
        if b < 0:
            b += MOD
        result += a * b
        result %= MOD

    return result


if __name__ == "__main__":
    N = int(input())
    L_A = list(map(int, input().split()))

    print(get_answer(N, L_A))
