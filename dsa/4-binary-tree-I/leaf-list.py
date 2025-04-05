# leaf list
# 
# Write a function, leaf_list, that takes in the root of a binary tree and returns a list
# containing the values of all leaf nodes in left-to-right order.
from Node import *# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque

def leaf_list(root):
    if not root:
        return []

    stack = deque([root])
    leaves = []

    while stack:
        current = stack.pop()
        
        if not current.left and not current.right:
            leaves.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return leaves



root = build_test_tree()
print_test_tree()
print(leaf_list(root)) # -> [ 'd', 'e', 'f' ] 

