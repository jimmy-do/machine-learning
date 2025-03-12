# Problem 1: Generate All Pairs (Easy)
# Given a list of numbers, print all unique pairs (a, b) where a appears before b in the list.

letters = ['a','b','c']

for i in range(len(letters)):
    for j in range(i+1,(len(letters))):
        print(i,j)

# Problem 2: Count Consecutive Duplicates (Medium)
# Given a string, compress it by replacing consecutive duplicate characters with their count.

s = "aaabbc"
i = 0
compressed = ''

while i < len(s):
    j = i + 1
    while j < len(s) and s[i]==s[j]:
        j += 1
    count = j - i
    compressed += (str(count) + s[i]) if count > 1 else s[i]
    i = j

print(compressed)
        
        