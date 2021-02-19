
from typing import List

def get_cumulative_sum_sequential(numbers: List[int]):
    """forで累積和を求める。
    This method works.
    """
    result: List[int] = [0]

    for number in numbers:
        sum = result[-1] + number
        result.append(sum)
    return result


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

