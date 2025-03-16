# pairs
# Write a function, pairs, that takes in a list as an argument. The function should return a list contain all unique pairs of elements.
# You may return the pairs in any order and the order of elements within a single pair does not matter.
# You can assume that the input list contains unique elements.

def pairs(ds):
    result = []

    for i in range(len(ds)):
        for j in range(i + 1, len(ds)):
            if ds[i] != ds[j]:
                result.append(ds[i])
                result.append(ds[j])
    return result


def pairs_using_set(ds):
    result = set()

    for i in range(len(ds)):
        for j in range(i + 1, len(ds)):
            if ds[i] != ds[j]:
                pair = (ds[i], ds[j])
                result.add(pair)

    return result


print(pairs(["a", "b", "c"]))
print(pairs_using_set(["a", "b", "c"]))
