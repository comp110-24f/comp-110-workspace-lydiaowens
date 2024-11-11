"""File to define River class."""

__author__ = "730671309"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """A River with Fish and Bears."""

    day: int
    fish = list[Fish]
    bears = list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove aged fish and bears from river."""
        surviving_fish = []
        surviving_bears = []
        for current_fish in self.fish:  # for each fish in list of fish
            if current_fish.age <= 3:
                surviving_fish.append(current_fish)  # add surviving bear
        for current_bear in self.bears:  # for each bear in list of bears
            if current_bear.age <= 5:
                surviving_bears.append(current_bear)  # add surviving bear
        self.fish = surviving_fish  # update river lists to only include surviving fish
        self.bears = (
            surviving_bears  # update river list to only include surviving bears
        )
        return None

    def remove_fish(self, amount: int):
        """Remove top fish from list for eating purposes."""
        idx: int = 0
        while idx < amount:  # index is less than number of fish being eaten
            self.fish.pop(0)  # removes first fish in list
            idx += 1
        return None

    def bears_eating(self):
        """Bears eating fish."""
        for bear in self.bears:
            if len(self.fish) > 4:
                self.remove_fish(3)  # 1 bear eating fish removes 3 fish
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks for starvation in bear."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:  # bear does not have negative hunger score
                surviving_bears.append(bear)
        self.bears = surviving_bears  # only keeps bears that did not starve
        return None

    def repopulate_fish(self):
        """Create more fish in river."""
        num_fish: int = len(self.fish)
        added_fish: int = (num_fish // 2) * 4  # calculate new fish from repopulation
        for i in range(added_fish):
            self.fish.append(Fish())  # add new fish to fish list
        return None

    def repopulate_bears(self):
        """Create more bears in river."""
        num_bears: int = len(self.bears)
        added_bears: int = num_bears // 2  # calculate new bears
        for i in range(added_bears):
            self.bears.append(Bear())  # add new bears to bear list
        return None

    def view_river(self):
        """Give counts of fish and bear populations on given days."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week in the river."""
        for i in range(7):  # runs one day simulation 7 times
            River.one_river_day(self)
        return None
