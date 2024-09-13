"Challenge Question 2 for COMP 110"

__author__ = "730671309"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(
        input("Guess a number: ")
    )  # takes guess as string, converts to int, and then stores in local variable x as an int
    print(
        "Your guess was " + str(x)
    )  # convert x back to string to print it, then concatenate with "Your guess was "

    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
