# all unique

# Write a function, all_unique, that takes in a list. The function should return a boolean
# indicating whether or not the list contains unique items.

def all_unique(items):
    items_set = set(items)
    return len(items)==len(items_set)

print(all_unique(["red", "blue", "blue", "green", "orange"]))