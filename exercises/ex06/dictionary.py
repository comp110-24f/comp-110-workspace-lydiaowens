"""Exercise 6: Dictionary Utility Functions"""

__author__ = "730671309"


# 1. invert function
def invert(dictionary: dict[str, str]) -> dict[str, str]:
    keysList = [
        key for key in dictionary
    ]  # capture dictionary keys from dictionary into one list
    # check if keysList has duplicates:
    for i in range(1, len(dictionary)):  # checks values after first value
        if dictionary[keysList[0]] == dictionary[keysList[i]]:  # if values match
            raise KeyError("Dictionaries cannot have duplicate keys!")
    # creating inverse dictionary
    idx: int = 0
    newdict: dict[str, str] = {}
    while idx < len(dictionary):
        newdict[dictionary[keysList[idx]]] = keysList[idx]
        # keysList[idx] = key, dictionary[keysList[idx]] = value, newdict[] assigns value to key
        idx += 1
    return newdict


# Testing invert
# my_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
# print(invert(my_dict))
# print(invert({"kris": "jordan", "michael": "jordan"}))


# 2. favorite colors
def favorite_color(dictionary: dict[str, str]) -> str:
    valuesList = []  # create list to extract colors
    for key in dictionary:
        valuesList.append(dictionary[key])
    if len(valuesList) == 0:
        return ""
    countingdictionary: dict[str, int] = {}  # make a new dictionary to count colors
    for item in valuesList:
        if item in countingdictionary:  # checking if color is in new dictionary
            countingdictionary[item] += 1
        else:
            countingdictionary[item] = 0  # sets initial count as zero

    # using countingdictionary to find favorite color
    favorite_color_count: int = 0  # set count of favorite color to zero
    for color in countingdictionary:
        if countingdictionary[color] > favorite_color_count:
            favorite_color_count = countingdictionary[color]
            favorite: str = color
    return favorite


# Testing favorite_colors
# print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


# count
def count(input: list[str]) -> dict[str, int]:
    countdict: dict[str, int] = {}
    for item in input:
        if item in countdict:
            countdict[item] += 1  # add to count
        else:
            countdict[item] = 1  # initialize item
    return countdict


# alphabetizer
def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    newdict: dict[str, list[str]] = {}
    for word in input:
        lower_word = word.lower()  # make word lowercase
        if lower_word[0] in newdict:  # if first letter of word is already key
            newdict[lower_word[0]].append(word)  # append non-lowercase word
        else:
            newdict[lower_word[0]] = [
                word,
            ]
    return newdict


# testing alphabetizer
# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))
# print(alphabetizer(["Python", "sugar", "Turtle", "party", "table"]))


# update_attendance
def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    if day in input:  # if day is a key in input dictionary
        for name in input[day]:  # checks for name in students already recorded
            if name == student:  # if student is already recorded
                return None  # do not alter dictionary
        input[day].append(student)  # otherwise record student
    else:
        input[day] = [
            student,
        ]
    return None


# Testing update_attendance
# ce_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# update_attendance(ce_log, "Tuesday", "Vrinda")
# print(ce_log)
# update_attendance(ce_log, "Wednesday", "Kaleb")
# print(ce_log)
