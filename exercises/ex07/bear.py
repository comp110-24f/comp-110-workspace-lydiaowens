"""File to define Bear class."""


class Bear:
    """A bear in the river with an age and hunger score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Bear with a certain age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Bear becomes 1 fish hungrier and 1 day older per day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Records number of fish eaten by bear in hunger score."""
        self.hunger_score += num_fish
        return None
