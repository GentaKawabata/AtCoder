"""
N進数の文字列を10進数に変換する
ans = int(str_base_no, n)
では、2 <= n <= 36 の制約あり
1文字で表せるのは、0-9 の10文字と、a-z の26文字だからかな～
ただしこの関数は、文字列を含むとエラー出る
"""
def base_n_to_10(str_base_no: str, n: int):
    result = 0
    for i, c in enumerate(str_base_no[::-1]):
        result += int(c) * (n**i)
    return result
