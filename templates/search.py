from typing import Any, List, NewType

Index = NewType("IndexNo", int)


def sequential(key: Any, arr: List[Any]) -> Index:
    if key in arr:
        for i, v in enumerate(arr):
            if v == key:
                return i
    else:
        return -1


def binary(key: Any, sorted_arr: List[Any]) -> Index:
    """
    sorted_arr の中から key の値を探索しその index を返す。
    見つからなかった場合は -1 を返す
    key となる値が配列内に重複している場合は...
    """

    left: int = 0
    right: int = len(sorted_arr) -1

    while (left <= right):
        mid: int = int(left + (right - left) / 2)
        # print(f"({left}, {mid}, {right})")
        if sorted_arr[mid] == key:
            return mid
        elif key < sorted_arr[mid]:
            right = mid - 1
        elif key > sorted_arr[mid]:
            left = mid + 1

    return -1
