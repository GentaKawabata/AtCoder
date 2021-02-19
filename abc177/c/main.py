# -*- coding: utf-8 -*-

from typing import List

MOD = int(1e9 + 7)

def get_cumulative_sum_sequential(numbers: List[int]):
    """forで累積和を求める。
    This method works.
    """
    result: List[int] = [0]

    for number in numbers:
        result.append(result[-1] + number)

    return result

def get_answer(n, l_a):

    l_c = get_cumulative_sum_sequential(l_a)
    result = 0
    for i in range(n - 1):
        a = l_a[i] % MOD
        b = (l_c[n] - l_c[i+1]) % MOD
        if b < 0:
            b += MOD

        # result = result % MOD + a * b % MOD
        result = result % MOD + a * b % MOD

    return result

if __name__ == "__main__":
    N = int(input())
    L_A = list(map(int, input().split()))

    print(get_answer(N, L_A))
