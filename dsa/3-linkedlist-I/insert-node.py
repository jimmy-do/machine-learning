from Node import * 
# insert node

# Write a function, insert_node, that takes in the head of a linked list, a value, and 
# an index. The function should insert a new node with the value into the list at the 
# specified index. Consider the head of the linked list as index 0. The function should 
# return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the 
# length of the input list.

def insert_node(head, value, index):
    # Case 1: Insertation right at the very front
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head
    
    # Traverse the list to find the node just BEFORE insertion point
    count = 0
    current = head
    
    while current:
        if count == index - 1:
            # We are at the node right before, time to insert
            temp = current.next             # Save next node
            current.next = Node(value)      # Insert new node after current
            current.next.next = temp        # Link new node to rest of list
            break                           # Insertion done
        count += 1
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
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
insert_node(a, 'x', 2)
# a -> b -> x -> c -> d
print_values(a)