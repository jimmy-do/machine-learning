from Node import *
# longest streak

# Write a function, longest_streak, that takes in the head of a linked list as an argument. 
# The function should return the length of the longest consecutive streak of the same value 
# within the list.

def longest_streak(head):
    max_streak = 0
    current_streak = 0
    prev_val = None
    current = head
    
    while current is not None:
        if current.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1
        
        if current_streak > max_streak:
            max_streak = current_streak
            
        prev_val = current.val
        current = current.next
    
    return max_streak



a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longest_streak(a)) # 3
