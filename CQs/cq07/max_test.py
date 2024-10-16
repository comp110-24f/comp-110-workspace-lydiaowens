"""Max Test"""

__author__ = "730671309"

from CQs.cq07.find_max import find_and_remove_max


def test_return_value() -> None:
    c: list[int] = [30, 28, 29, 27, 30, 5]
    assert find_and_remove_max(c) == 30


def test_mutate() -> None:
    c: list[int] = [30, 28, 29, 27, 30, 5]
    find_and_remove_max(c)
    assert c == [28, 29, 27, 5]


def test_unconventional() -> None:
    input: list[str] = []
    assert find_and_remove_max(input) == -1
