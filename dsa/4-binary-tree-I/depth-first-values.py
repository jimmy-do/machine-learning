from Node import *
# depth first values

# Write a function, depth_first_values, that takes in the root of a binary tree. The function 
# should return a list containing all values of the tree in depth-first order.

# Hey. This is our first binary tree problem, so you should be liberal with watching the Approach 
# and Walkthrough. Be productive, not stubborn. -AZ

def depth_first_values(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result



print(depth_first_values(a))

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
