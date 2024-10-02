"""Coordinates"""

__author__ = "730671309"


def get_coords(xs: str, ys: str) -> None:
    counter1 = 0
    while counter1 < len(xs):
        coord1 = xs[counter1]
        counter2 = 0
        while counter2 < len(ys):
            coord2 = ys[counter2]
            print("(" + coord1 + "," + coord2 + ")")
            counter2 += 1
        counter1 += 1
    return None
