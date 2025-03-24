from Node import *
# zipper lists

# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. 
# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

def zipper_lists_iteratively(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0
    
    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1
        
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2

    return head1


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")



# Create list A: a -> b -> c
a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c

# Create list B: x -> y -> z -> w
x = Node('x')
y = Node('y')
z = Node('z')
w = Node('w')
x.next = y
y.next = z
z.next = w

# Zipper them
result = zipper_lists_iteratively(a, x)
print_list(result)
