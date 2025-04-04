from collections import deque
from Node import *
# tree levels

# Write a function, tree_levels, that takes in the root of a binary tree. The function should return 
# a 2-Dimensional list where each sublist represents a level of the tree.

def tree_levels(root):
    if not root:
        return []

    levels = []
    queue = deque([(root,0)])

    while queue:
        current, level = queue.popleft()

        if len(levels) == level:
            levels.append([current.val])
        else:
            levels[level].append(current.val)
    
        if current.left:
            queue.append((current.left, level + 1))
        if current.right:
            queue.append((current.right, level + 1))

    return levels

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.left = b
a.right = c
b.left = d
c.right = e

print(tree_levels(a))
