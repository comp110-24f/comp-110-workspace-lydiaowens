"""File to define Fish class."""


class Fish:
    """A fish in the river with a certain age."""

    age: int

    def __init__(self):
        """Fish with a certain age."""
        self.age = 0
        return None

    def one_day(self):
        """Fish becomes 1 day older."""
        self.age += 1  # fish ages 1 day
        return None
