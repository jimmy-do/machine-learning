# compress
# 
# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where
# consecutive occurrences of the same characters are compressed into the
# number of occurrences followed by the character. Single character occurrences 
# should not be changed.

def compress(s):
    i = 0
    compressed = ''
    while i < len(s):
        j = i + 1
        while j < len(s) and s[i]==s[j]:
            j += 1
        count = j - 1
        compressed += (str(count) + s[i]) if count > 1 else s[i]
        i = j
    return compressed


print(compress('ssssbbz')) # -> '4s2bz'
