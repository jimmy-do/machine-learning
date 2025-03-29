from collections import deque
from Node import *
# tree sum

# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
# The function should return the total sum of all values in the tree.

def tree_sum_iterative(root):
    if not root:
        return 0
    queue = deque([root])
    sum = 0
    while queue:
        current = queue.popleft()
        sum += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum


def tree_sum_recursive(root):
    if not root:
        return 0
    return root.val + tree_sum_recursive(root.left) + tree_sum_recursive(root.right)


        
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

print(tree_sum_iterative(a)) # -> 21
print(tree_sum_recursive(a)) # -> 21
