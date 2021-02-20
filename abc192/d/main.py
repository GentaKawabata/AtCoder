# -*- coding: utf-8 -*-


def base_n_to_10(x: str, n: int):
    result = 0
    num = len(str(x)) + 1
    for i in range(1, num):
        result += int(x[-i]) * (n**(i-1))
    return result


def get_answer(x: str, m: int):
    list_str_no = list(x)

    list_no = list(map(lambda x: int(x), list_str_no))
    d = max(list_no)

    result = 0
    n = d + 1
    while True:
        number_x = base_n_to_10(x, n)
        if number_x <= m:
            result += 1
        else:
            break
        n += 1
    return result


if __name__ == "__main__":
    X = input()
    M = int(input())

    print(get_answer(X, M))
