from Node import *
# get node value

# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

def get_node_value(head, index):
    current = head
    count = 0
    while current:
        if count == index:
            return current.val
        count += 1
        current = current.next
    return None

def get_node_value_recursive(head, index):
    if not head:
        return False
    if index == 0:
        return head.value
    return get_node_value_recursive(head.next, index - 1)




a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'
print(get_node_value_recursive(a, 2)) # 'c'
