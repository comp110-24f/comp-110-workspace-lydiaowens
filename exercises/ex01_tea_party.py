"""Exercise 1: Tea Party"""

__author__: str = "730671309"


def main_planner(
    guests: int,
) -> None:  # Displays an output for a tea party, including tea treats and costs
    """Runs all functions and prints output of tea party"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:",
        "$"
        + str(
            cost(
                tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
            )  # concatenates to remove space between $ sign and number!
        ),
    )
    return None


def tea_bags(people: int) -> int:
    """Return the number of teabags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """Determining the number of treats needed based on tea"""
    return int(
        tea_bags(people=people) * 1.5
    )  # rounds up treats to whole number (integer)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns costs of tea bags and treats"""
    return (
        0.5 * tea_count + 0.75 * treat_count
    )  # will need to call functions in arguments of this function


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # allows user to change number of guests for party and recalculate variables
