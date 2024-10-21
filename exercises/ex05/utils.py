"""Utilization Functions"""

__author__ = "730671309"


# 1. only_evens function
def only_evens(input: list[int]) -> list[int]:
    even_list: list[int] = []  # making empty new list
    if len(input) == 0:
        return even_list  # returns empty list if given empty list
    for item in input:
        if item % 2 == 0:
            even_list.append(item)
    return even_list


# sub function
def sub(input: list[int], index_1: int, index_2: int) -> list[int]:
    subset_list: list[int] = []  # creating new list
    if len(input) == 0 or index_1 >= len(input) or index_2 <= 0:
        return subset_list  # returns empty list
    start_index: int = index_1
    end_index: int = index_2
    if index_1 < 0:  # start index is negative
        start_index: int = 0  # start from beginnning of list
    if index_2 > len(input):  # end index is greater than length of list
        end_index: int = len(input)  # ends with end of list
    for i in range(start_index, end_index):
        subset_list.append(input[i])
    return subset_list


# add_at_index function
def add_at_index(input: list[int], item: int, item_index: int) -> None:
    if item_index < 0 or item_index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    inputcopy: list[int] = input  # preserve original indexes
    input.append(0)  # make space to add new item
    shift_counter: int = len(inputcopy) - 1  # shifts item to right starting at the end
    while shift_counter > item_index:  # shifts until index = given item_index
        input[shift_counter] = inputcopy[
            shift_counter - 1
        ]  # moves each item right once
        shift_counter = shift_counter - 1

    input[item_index] = item  # insert new item in correct spot
    return None
