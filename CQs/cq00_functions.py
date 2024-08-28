""" Challenge Question 00 for COMP 110"""

__author__ = "730671309"


def mimic(message: str) -> str:
    """Will take the input and repeat it back as a string"""
    return message


def main() -> None:
    """A function to pull together your functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
