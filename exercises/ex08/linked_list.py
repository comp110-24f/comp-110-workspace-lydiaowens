"""Linked List Examples from Class for EX08."""

from __future__ import annotations

__author__ = "730671309"


class Node:
    """Nodes with values and connections."""

    value: int  # nodes and integers
    next: Node | None  # goes to another node or none

    def __init__(
        self, value: int, next: Node | None
    ):  # within this class, we have itself, value and next
        """Each node in class has value and next."""
        self.value = value
        self.next = next

    def __str__(
        self,
    ) -> str:  # example of magic method-> represents objects as a string
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: figure out rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


# initializing nodes
two: Node = Node(2, None)  # two is a node with value 2 which connects to nothing
one: Node = Node(1, two)  # one is a node with value 1 which connects to Node 2
# one_two: Node = Node(1, Node(2, None)) does what Lines 18-19 does
courses: Node = Node(
    110, Node(210, Node(301, None))
)  # Node 110 which connects to 210 which connects to 301 which connects to nothing


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # base case: when head is the last node
    # return its value
    # Recursive case:
    # Figure out the last node (recursive call) in the rest of the list
    # Return this value!
    print(f"Enter last({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    else:
        rest: int = last(head.next)  # recursive call
        print(f"Return recur: {head.value} -> {rest}")
        return rest


# Exercise 8 Specific Code:


# value_at function
def value_at(head: Node | None, index: int) -> int:
    """Returns value of Node stored at given index or raises and IndexError."""
    # Base case:
    # List is empty
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Index is 0
    if index == 0:
        return head.value
    # Recursive
    else:
        value: int = value_at(head.next, index - 1)
        return value


# Testing value_at function
# print(value_at(Node(10, Node(20, Node(30, None))), 0))
# print(value_at(Node(10, Node(20, Node(30, None))), 1))
# print(value_at(Node(10, Node(20, Node(30, None))), 2))
# print(value_at(Node(10, Node(20, Node(30, None))), 3))


# max function
def max(head: Node | None) -> int:
    """Given a head node, returns the maximum value in the linked list. If the linked list is empty, raise a ValueError."""
    if head is None:
        raise ValueError("Cannot call max with None")

    if head.next is None:  # if reached last value in list
        return head.value

    rest_max = max(head.next)  # value of next head will be max unless

    return (
        head.value if head.value > rest_max else rest_max
    )  # current head value is higher than next head value


# Testing Max Function
# print(max(Node(10, Node(20, Node(30, None)))))
# print(max(Node(10, Node(30, Node(20, None)))))
# print(max(Node(30, Node(20, Node(10, None)))))
# print(max(None))

# Linkify


def linkify(items: list[int]) -> Node | None:
    """Given a list[int], return a Linked List of Nodes with the same values, in the same order, as the input list."""
    # base case- list is empty:
    if items == []:
        return None

    # recursive case- head is first item and next is next item in list:
    return Node(
        items[0], linkify(items[1:])
    )  # calls linkify to return next node until reaches end of the list


# print(linkify([1, 2, 3]))


# scale function
def scale(head: Node | None, factor: int) -> Node | None:
    """Return Linked List scaled by Factor."""
    # base case- list is empty:
    if head is None:
        return None

    new_head = Node(head.value * factor, None)  # create new node with scaled value
    new_head.next = scale(head.next, factor)  # scale next node
    return new_head


# print(scale(linkify([1, 2, 3]), 2))
