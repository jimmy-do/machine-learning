from Node import *
from collections import deque
# tree value count
# 
# Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

def tree_value_count(root, target):
    if not root:                    # base case
        return None
    
    stack = deque([root])           # initialize variables 
    count = 0

    while stack:                    # while loop to go over stack
        current = stack.pop()       # establish current var, link to count logic
        if current.val == target:
            count += 1
        if current.left:
            stack.append(current.left)   # add more nodes to stack as we descend tree
        if current.right:
            stack.append(current.right) # ensure we traverse down both left and right child nodes
    return count



root = build_test_tree_nums()
print_test_tree_nums()
print(tree_value_count(root, 6))
