from collections import deque
from Node import *
# tree min value

# Write a function, tree_min_value, that takes in the root of a binary tree that contains 
# number values. The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.

def tree_min_value_iterative(root): #breadth first search
    minimum = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.val < minimum:
            minimum = current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return minimum


def tree_min_value_recursive(root):
   if not root:
       return float("inf") 
   smallest_left = tree_min_value_recursive(root.left)
   smallest_right = tree_min_value_recursive(root.right)
   return min(root.val,smallest_left,smallest_right)



a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
print(tree_min_value_iterative(a)) 
print(tree_min_value_recursive(a)) 