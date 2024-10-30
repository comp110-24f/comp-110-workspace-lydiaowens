def insert_float(lst: list[float], index: int, num: float) -> list[float]:
    result: list[float] = []

    for x in range(0, len(lst)):
        if x == index:
            result.append(num)
        result.append(lst[x])

    if index >= len(lst):
        result.append(num)
    return result


print(insert_float([3.0, 4.0, 2.0], 1, 5.0))
