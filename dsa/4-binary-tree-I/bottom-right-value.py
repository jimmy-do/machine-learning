from Node import *
from collections import deque
# bottom right value
#
# Write a function, bottom_right_value, that takes in the root of a binary tree.
# The function should return the right-most value in the bottom-most level of the tree.
#
# You may assume that the input tree is non-empty.

def bottom_right_value(root):
    if not root:
        return None

    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return current.val


def bottom_right_value_sysout(root):
    if not root:
        print("🌵 Tree is empty. No bottom-right value.")
        return None

    queue = deque([root])
    print(f"🚀 Starting BFS with root: {root.val}")

    while queue:
        current = queue.popleft()
        print(f"🔍 Visiting node: {current.val}")

        if current.left:
            print(f"👈 Adding left child to queue: {current.left.val}")
            queue.append(current.left)
        if current.right:
            print(f"👉 Adding right child to queue: {current.right.val}")
            queue.append(current.right)

    print(f"🎯 Bottom-right value found: {current.val}")
    return current.val



a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \
#    -2  6

print(bottom_right_value(a)) # -> 6
print(bottom_right_value_sysout(a)) # -> 6

