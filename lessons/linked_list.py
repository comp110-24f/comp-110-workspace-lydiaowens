"""Linked List Examples from Class for EX08"""

from __future__ import annotations


class Node:
    value: int  # nodes and integers
    next: Node | None  # goes to another node or none

    def __init__(
        self, value: int, next: Node | None
    ):  # within this class, we have itself, value and next
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

print(one)
print(str(courses))
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list"""
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


print(last(one))  # Expect to print 2
print(last(courses))  # Expect to print 301
