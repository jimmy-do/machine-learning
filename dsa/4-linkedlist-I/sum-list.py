from Node import *
# sum list
#
# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
# The function should return the total sum of all values in the linked list.

def sum_list(head):
    result = 0
    current = head
    while current:
        result += current.val
        current = current.next
    return result

def sum_list_recursive(head):
    if not head:
        return 0
    return head.val + sum_list_recursive(head.next)


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19
print(sum_list_recursive(a)) # 19
