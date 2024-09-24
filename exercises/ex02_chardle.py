"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730671309"


# part 6: putting everything together
def main() -> (
    None
):  # main calls all of the functions defined below and starts Chardle game
    contains_char(word=input_word(), letter=input_letter())
    return None


# part 1: define a function input_word + part 5: implementing exits
def input_word() -> str:
    """Function takes word as input from user and returns said word"""
    word = str(
        input("Enter a 5-character word: ")
    )  # takes 5 char word from user and stores as a str local variable called word

    if len(word) != 5:  # checks to see if the word is exactly 5 characters
        print("Error: Word must contain 5 characters.")
        exit()
        return word
    else:
        return word


# part 2: define a function input_letter + part 5: implementing exits
def input_letter() -> str:
    """Function takes a single character as input from user and returns said character"""
    char = str(
        input("Enter a single character: ")
    )  # takes single char as a str local variable called char

    if len(char) != 1:  # checks to see if the character is just one character
        print("Error: Character must be a single character.")
        exit()
        return char
    else:
        return char


# part 3 and part 4: checking indices for matches and counting match indices
def contains_char(
    word: str, letter: str
) -> None:  # takes in word and letter and returns nothing
    """Function that intakes word and letter, then iterates through word to see if letter matches word's letter and reports results"""
    print("Searching for", letter, "in", word)
    index: int = 0  # creates variable index to count index of word, starting at 0
    instances: int = (
        0  # variable for counting the number of times letter is found in word
    )
    while index < len(
        word
    ):  # creates a while loop to loop through each character of word
        if (
            letter == word[index]
        ):  # indexes word at given index and sees if the 2 letters match
            print(letter, "found at index", index)  # reports the match
            index += 1
            instances += 1
        else:
            index += 1  # skips to next index to check next letter
    if instances == 0:
        print(
            "No instances of", letter, "found in", word
        )  # if there are no instances, tells user there are none
    else:
        print(
            instances, "instances of", letter, "found in", word
        )  # if there are instances, tells user how many there are
    return None


if __name__ == "__main__":
    main()
