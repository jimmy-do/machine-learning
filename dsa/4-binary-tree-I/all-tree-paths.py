from Node import *
# Write a function, all_tree_paths, that takes in the root of a binary tree. 
# The function should return a 2-Dimensional list where each subarray represents 
# a root-to-leaf path in the tree.
# 
# The order within an individual path must start at the root and end at the leaf,
# but the relative order among paths in the outer list does not matter.
# 
# You may assume that the input tree is non-empty.

def all_tree_paths(root):
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse()
    return paths

def _all_tree_paths(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]
    all_paths = []
    left_sub_paths = _all_tree_paths(root.left)
    for path in left_sub_paths:
        path.append(root.val)
        all_paths.append(path)
    right_sub_paths = _all_tree_paths(root.right)
    for path in right_sub_paths:
        path.append(root.val)
        all_paths.append(path)
    return all_paths

root = build_test_tree()
print_test_tree()
print(all_tree_paths(root))

