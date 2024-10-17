"""Summing the elements of a list using different loops"""

__author__ = "730671309"

# part 1. w_sum()


def w_sum(vals: list[float]) -> float:
    if len(vals) == 0:
        return 0.0
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


print(w_sum(vals=[1.1, 0.9, 1.0]))


# part 2. f_sum()
def f_sum(vals: list[float]) -> float:
    if len(vals) == 0:
        return 0.0
    sum: float = 0.0
    for value in vals:
        sum += value
    return sum


print(f_sum(vals=[1.1, 0.9, 1.0]))


# part 3. r_range_sum()
def f_range_sum(vals: list[float]) -> float:
    if len(vals) == 0:
        return 0.0
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum += vals[index]
    return sum


print(f_range_sum(vals=[1.1, 0.9, 1.0]))
