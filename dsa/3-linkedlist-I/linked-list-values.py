from Node import *

# linked list values
#
# Write a function, linked_list_values, that takes in the head of a linked list as an argument.
# The function should return a list containing all values of the nodes in the linked list.
#
# Hey. This is our first linked list problem, so you should be liberal with watching the
# Approach and Walkthrough. Be productive! -AZ


def linked_listed_values(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_listed_values(a)) # -> [ 'a', 'b', 'c', 'd' ]
