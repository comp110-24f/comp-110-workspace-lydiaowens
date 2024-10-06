"""Mutating functions."""

__author__ = "730671309"


def manual_append(val: list[int], num: int) -> None:
    val.append(num)
    return None


def double(doublelist: list[int]) -> None:
    index: int = 0  # counter for doubling
    while index < len(doublelist):
        doublelist[index] = 2 * int(doublelist[index])
        index += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
