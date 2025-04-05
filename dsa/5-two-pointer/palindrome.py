# is palindrome
# 
# Write a function, is_palindrome, that takes in a string and returns a boolean indicating whether
# or not the string is the same forwards and backwards.

def palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


print(palindrome('racecar'))

