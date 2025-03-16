# exclusive items
#
# Write a function, exclusive_items, that takes in two lists, a,b, as arguments.
# The function should return a new list containing elements that are in either list but not both lists.
#
# You may assume that each input list does not contain duplicate elements.

def exclusive_items(listy1,listy2):
    result = []
    for i in listy1:
        if i not in listy2:
            result.append(i)

    for j in listy2:
        if j not in listy1:
            result.append(j)

    return result

def exclusive_items_using_set(a,b):
    result = []
    set_a = set(a)
    set_b = set(b)
    for i in set_a:
        if i not in set_b:
            result.append(i)
    for i in set_b:
        if i not in set_b:
            result.append(i)
    return result        


print(exclusive_items([4,2,1,6], [3,6,9,2,10]))

a = [ i for i in range(0, 5) ]
b = [ i for i in range(0, 5) ]

print(exclusive_items(a,b))

