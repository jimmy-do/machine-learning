from Node import *
# how high

# Write a function, how_high, that takes in the root of a binary tree. The function should 
# return a number representing the height of the tree.

# The height of a binary tree is defined as the maximal number of edges from the root node 
# to any leaf node.

# If the tree is empty, return -1.

def how_high(node):
    if not node:
        return -1
    
    left_height = how_high(node.left)
    right_height = how_high(node.right)

    return 1 + max(left_height,right_height)


def how_high_sysout(node, depth=0):
    indent = "  " * depth  # Indentation for visual hierarchy

    if node is None:
        print(f"{indent}🌱 None node → returning -1")
        return -1

    print(f"{indent}🔍 Visiting node '{node.val}' at depth {depth}")

    left_height = how_high_sysout(node.left, depth + 1)
    right_height = how_high_sysout(node.right, depth + 1)

    height = 1 + max(left_height, right_height)
    print(f"{indent}🌳 Node '{node.val}': left = {left_height}, right = {right_height} ➜ height = {height}\n\n")

    return height



root = build_test_tree()
print_test_tree()
how_high_sysout(root)

