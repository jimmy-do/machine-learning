# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

def intersection(a,b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result


# print(intersection([4,2,1,6], [3,6,9,2,10]))
a = [ i for i in range(0, 5) ]
b = [ i for i in range(0, 5) ]
print(intersection(a, b)) # -> [0,1,2,3,..., 49999]
