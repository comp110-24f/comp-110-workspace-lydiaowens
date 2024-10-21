"""Unit Tests for Utilization Functions"""

__author__ = "730671309"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# only_evens tests
def test_only_evens_edge() -> None:
    """Tests if only_evens returns an empty list if given one"""
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_use_return() -> None:
    """Tests if only_evens returns only even integers from a given list"""
    b: list[int] = [3, 4, 6, 7, 12, 15]
    assert only_evens(b) == [4, 6, 12]


def test_only_evens_use_mutate() -> None:
    """Tests if only_evens does not mutate its input list"""
    b: list[int] = [3, 4, 6, 7, 12, 15]
    only_evens(b)
    assert b == [3, 4, 6, 7, 12, 15]


# sub tests
def test_sub_edge() -> None:
    """Tests if sub returns an empty list if given faulty indices"""
    f: list[int] = [8, 10, 12, 14, 16, 18, 20]
    assert sub(f, 10, 12) == []


def test_sub_use_return() -> None:
    """Tests if sub returns list items within the given indices"""
    f: list[int] = [8, 10, 12, 14, 16, 18, 20]
    assert sub(f, 2, 4) == [12, 14]


def test_sub_use_mutate() -> None:
    """Tests if sub does not mutate its input list"""
    f: list[int] = [8, 10, 12, 14, 16, 18, 20]
    sub(f, 1, 3)
    assert f == [8, 10, 12, 14, 16, 18, 20]


# add_at_index tests
def test_add_at_index_use_return() -> None:
    """Tests if add_at_index correctly returns nothing"""
    d: list[int] = [2, 6, 8, 10]
    assert add_at_index(d, 4, 1) == None


def test_add_at_index_use_mutate() -> None:
    """Tests if add_at_index mutates its given list"""
    d: list[int] = [2, 6, 8, 10]
    add_at_index(d, 4, 2)
    assert d == [2, 6, 4, 8, 10]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    e: list[int] = [4, 5, 6]  # object to pass at add_at_index
    with pytest.raises(IndexError):
        add_at_index(e, 7, 5)
