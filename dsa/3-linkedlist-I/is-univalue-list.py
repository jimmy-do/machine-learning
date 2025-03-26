from Node import *
# is univalue list

# Write a function, is_univalue_list, that takes in the head of a linked list as 
# an argument. The function should return a boolean indicating whether or not the
# linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

def is_univalue_list_iterative(head):
    if not head:
        return True
    
    current = head
    while current:
        if current.val != head.val:
            return False
        current = current.next
    return True


def is_univalue_recursive(head, prev_val=None):
    current = head
    if not current:
        return True
    if prev_val is None or current.val == prev_val:
        return is_univalue_recursive(current.next, current.val)
    else:
        return False



a = Node(7)
b = Node(7)
c = Node(111)

a.next = b
b.next = c

# 7 -> 7 -> 111

print(is_univalue_list_iterative(a)) # False
