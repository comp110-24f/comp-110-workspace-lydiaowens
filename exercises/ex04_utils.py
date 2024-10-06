"""Exercise 4: List Utility Functions"""

__author__ = "730671309"


# 1. all function
def all(int_list: list[int], number: int) -> bool:
    index: int = 0  # counter to index each value of int_list
    if len(int_list) == 0:
        return False  # returns false if given list is empty
    while index < len(int_list):
        if (
            int_list[index] != number
        ):  # if number is not the same, should immediately return false
            return False
        index += 1
    return True  # if all match, function returns true


# 2. max function
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # raises error if list is empty
    index: int = 0  # counter to index each value of input
    max_number: int = input[index]  # starts with max value being the first value
    while index < (
        len(input) - 1
    ):  # len-1 as second to last number is compared to last number
        if max_number < input[index + 1]:
            max_number = input[index + 1]  # if next number is larger, next number = max
        index += 1  # goes to next number
    return max_number


# 3. is_equal function
def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):  # checks if lengths of lists are equal
        return False
    index: int = 0  # index to iterate through list values
    while index < len(list1):
        if (
            list1[index] != list2[index]
        ):  # if numbers do not match, immediately returns False
            return False
        if list1[index] == list2[index]:
            index += 1  # skips to check next value
    return True


# 4. extend function
def extend(list1: list[int], list2: list[int]) -> None:
    index: int = 0  # index to iterate through list2 elements
    while index < len(list2):
        list1.append(list2[index])  # appends each item from list2 to list1
        index += 1
    return None
