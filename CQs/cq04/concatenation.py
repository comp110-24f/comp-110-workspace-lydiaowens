"""Concatenation"""

__author__ = "730671309"


def main() -> None:
    print(concat("happy", "tuesday"))
    return None


def concat(str1: str, str2: str) -> str:
    word = str1 + str2
    return word


word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":
    main()
