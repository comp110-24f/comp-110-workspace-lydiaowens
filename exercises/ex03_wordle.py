"""Exercise 3 - Wordle"""

__author__ = "730671309"


# Part 1. input_guess
def input_guess(secret_word_len: int) -> str:
    guessed_word = input(
        f"Enter a {secret_word_len} character word: "  # uses f-string to enter in secret word length
    )  # should change number based on length of integer parameter
    while len(guessed_word) != secret_word_len:
        guessed_word = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # lets user guess again
    return guessed_word  # returns first guess with correct length


# Part 2. contains_char
def contains_char(secret_word: str, char_guess: str) -> bool:
    """Tests if char is contained in searchstring, returning True if so and False if not"""
    assert len(char_guess) == 1
    counter: int = 0  # counter for index referencing
    while counter < len(secret_word):
        if secret_word[counter] == char_guess:
            return True
        else:
            counter += 1  # goes to next index
    return False  # after all indexes are searched and no match, returns false


# Part 3. emojified
def emojified(guess: str, secret: str) -> str:
    """Function returns string of emojis giving matching clues based off of user's guess"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    returnstring: str = ""  # makes empty return string to keep emoji boxes
    index: int = 0  # index to test secret word
    while index < len(secret):
        if guess[index] == secret[index]:  # match in the right location
            returnstring += GREEN_BOX
        else:
            if (
                contains_char(secret, guess[index]) == True
            ):  # contains char but is in wrong location
                returnstring += YELLOW_BOX
            if contains_char(secret, guess[index]) == False:  # is not in guess word
                returnstring += WHITE_BOX
        index += 1
    return returnstring  # contains all matching info


# Part 4. main
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # counts turns of the game
    while turn <= 6:  # while the game is in session
        print(f"=== Turn {turn}/6 ===")
        guessed_word = input_guess(
            secret_word_len=len(secret)
        )  # takes guessed_word as variable from user
        print(emojified(guessed_word, secret))  # shows matching clues
        if guessed_word == secret:  # ends game (win)
            print(f"You won in {turn}/6 turns!")
            return None
        else:
            turn += 1  # continues game
    print(
        "X/6 - Sorry, try again tomorrow!"
    )  # user has no more turns left, so ends game
    return None


if __name__ == "__main__":
    main(secret="codes")
