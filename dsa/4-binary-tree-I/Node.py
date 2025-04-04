from __future__ import annotations
from typing import Optional, Union

class Node:
    val: Union[str, int]
    left: Optional[Node]
    right: Optional[Node]

    def __init__(self, val: Union[str, int]) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node({self.val!r})"
        
def build_test_tree():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def build_test_tree_nums():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a


def print_test_tree():
    print("     a")
    print("   /   \\")
    print("  b     c")
    print(" / \\     \\")
    print("d   e     f")
    print("\n" * 2)

def print_test_tree_nums():
    print("     12")
    print("   /   \\")
    print("  6     6")
    print(" / \\     \\")
    print("4   6     12")
    print("\n" * 2)
