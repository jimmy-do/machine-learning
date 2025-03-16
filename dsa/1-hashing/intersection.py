# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list
# containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

def intersection_brute(first_list, second_list):
    result = []
    for i in first_list:
        if i in second_list:
            result.append(i)
    return result


def intersection_using_set(first_list, second_list):
    pass


# print(intersection([4,2,1,6], [3,6,9,2,10]))
a = [i for i in range(0, 5)]
b = [i for i in range(0, 5)]
print(intersection_brute(a, b))
