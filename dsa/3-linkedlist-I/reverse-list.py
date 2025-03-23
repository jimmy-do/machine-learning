from Node import *
# reverse list

# Write a function, reverse_list, that takes in the head of a linked list as an argument. 
# The function should reverse the order of the nodes in the linked list in-place and return 
# the new head of the reversed linked list.

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def reverse_linked_list_recursive(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_linked_list_recursive(next, head)


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
print_linked_list(a)
print(reverse_linked_list(a)) # f -> e -> d -> c -> b -> a
print_linked_list(f)
print(reverse_linked_list_recursive(f))

