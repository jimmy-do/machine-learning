# intersection with dupes
#
# Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments.
# The function should return a new list containing elements that are common to both input lists.
# The elements in the result should appear as many times as they occur in both input lists.
#
# You can return the result in any order.
from collections import Counter

def intersection_with_dupes(a,b):
    # count_a = Counter(a)
    # count_b = Counter(b)
    # result = []
    # for ele in count_a:
    #     for i in range(0, min(count_a[ele], count_b[ele])):
    #         result.append(ele)
    # return result
    # result = count_a & count_b
    # return list(result.elements())
    return list((Counter(a) & Counter(b)).elements())



print(intersection_with_dupes(
  ["a", "b", "c", "b"],
  ["x", "y", "b", "b"]
)) # -> ["b", "b"]))

print(intersection_with_dupes(
  ["q", "b", "m", "s", "s", "s"],
  ["s", "m", "s"]
)) # -> ["m", "s", "s"]

print(intersection_with_dupes(
  ["p", "r", "r", "r"],
  ["r"]
)) # -> ["r"]