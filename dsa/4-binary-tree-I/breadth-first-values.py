from collections import deque
from Node import *
# breadth first values

# Write a function, breadth_first_values, that takes in the root of a binary
# tree. The function should return a list containing all values of the tree in 
# breadth-first order.

def breadth_first_values(root):
    if not root:
        return []
    
    queue = deque([root]) # F.I.F.O
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def print_nodes(nodey):
    for nodes in nodey:
        print(f"(Node: '{nodes}')",end=" --> ")



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

print(breadth_first_values(a))
print_nodes(breadth_first_values(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
