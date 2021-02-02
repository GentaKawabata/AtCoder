from typing import List

"""
 10進を2進数に変換
 dec_no: 10進数
 digit: 桁数

 dec_to_bin(3, 3) -> [0, 1, 1]
 dec_to_bin(3, 4) -> [0, 0, 1, 1]

 ※ 桁数が足りない場合は実装できていない
 dec_to_bin(3, 1) -> エラー
 """


def dec_to_bin(dec_no: int, digit: int) -> List[int]:
    result: List[int] = [0 for _ in range(digit)]

    counter = 0
    while dec_no != 0:
        result[digit - 1 - counter] = dec_no % 2
        dec_no = dec_no // 2
        counter += 1
    return result
