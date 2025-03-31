from Node import *
from collections import deque
# tree path finder

# Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

# You may assume that the tree contains unique values.

def path_finder_slow(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return [root.val]

    left_path = path_finder_slow(root.left, target)
    if left_path:
        return [root.val, *left_path]

    right_path = path_finder_slow(root.right, target)
    if right_path:
        return [root.val, *right_path]
    
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(path_finder_slow(a, 'e')) # -> [ 'a', 'b', 'e' ]
print(path_finder_fast(a, 'e')) # -> [ 'a', 'b', 'e' ]

