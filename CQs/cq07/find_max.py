"""Find Max"""

__author__ = "730671309"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    index: int = 0
    max_number: int = input[index]
    while index < (len(input) - 1):
        if max_number < input[index + 1]:
            max_number = input[index + 1]
        index += 1
    # removing maximum
    index2: int = 0
    while index2 < len(input):
        if input[index2] == max_number:
            input.pop(index2)
        else:
            index2 += 1
    return max_number


b: list[int] = [10, 9, 8, 7, 10]
print(find_and_remove_max(b))
print(b)

a: list[int] = []
print(find_and_remove_max(a))

c: list[int] = [1, 8, 8, 3, 3]
find_and_remove_max(c)
print(c)
