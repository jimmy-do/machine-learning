from Node import *
from collections import deque
# tree path finder

# Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

# You may assume that the tree contains unique values.

def path_finder_plus(root, target):
    if root is None:
        print("Reached a None node, returning None")
        return None

    print(f"Visiting Node: {root.val}")

    if root.val == target:
        print(f"Found target {target} at node {root.val}")
        return [root.val]

    print(f"Searching left of {root.val}")
    left_path = path_finder_plus(root.left, target)
    if left_path is not None:
        path = [root.val] + left_path
        print(f"Path found via left of {root.val}: {path}")
        return path

    print(f"Searching right of {root.val}")
    right_path = path_finder_plus(root.right, target)
    if right_path is not None:
        path = [root.val] + right_path
        print(f"Path found via right of {root.val}: {path}")
        return path

    print(f"No path found from node {root.val}, returning None")
    return None


def path_finder_fast(root, target):
  result = _path_finder_fast(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder_fast(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = _path_finder_fast(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  
  right_path = _path_finder_fast(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  
  return None



root = build_test_tree()
print_test_tree()

print(path_finder_plus(root, 'e')) # -> [ 'a', 'b', 'e' ]
print(path_finder_fast(root, 'e')) # -> [ 'a', 'b', 'e' ]

