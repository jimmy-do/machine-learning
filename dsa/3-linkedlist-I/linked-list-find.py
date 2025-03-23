from Node import *
# linked list find

# Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
# The function should return a boolean indicating whether or not the linked list contains the target.

def linked_list_find(head, target_val):
    current = head
    while current:
        if current.val == target_val:
            return True
        current = current.next
    return False


def linked_list_find_recursive(head, target_val):
    if not head:
        return False
    if head.val == target_val:
        return True
    return linked_list_find_recursive(head.next, target_val)



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "C")) # True
