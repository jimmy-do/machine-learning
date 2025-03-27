from Node import *
# remove node

# Write a function, remove_node, that takes in the head of a linked list and a target 
# value as arguments. The function should delete the node containing the target value 
# from the linked list and return the head of the resulting linked list. If the target 
# appears multiple times in the linked list, only remove the first instance of the target 
# in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

def remove_node_iterative(head, target_val):
    current = head
    prev = None
    
    if current.val == target_val:
        return current.next
    
    while current:
        if current.val == target_val:
            prev.next = current.next
            # break
        prev = current
        current = current.next

    return head


def print_values(current):
    while current:
        print(f"{current.val}",end="->")
        current = current.next
    print("None")
 
 
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("c")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print_values(remove_node_iterative(a, "c"))
# a -> b -> d -> e -> f
