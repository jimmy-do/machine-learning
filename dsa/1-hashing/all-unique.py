# all unique

# Write a function, all_unique, that takes in a list. The function should return a boolean
# indicating whether or not the list contains unique items.

def all_unique(items):
    items_set = set(items)
    if len(items) == len(items_set):
        return True
    else:
        return False
    
    