def compress(s):
    s += '!'  # Append a sentinel character to handle the last group of characters.
    result = ''  # Initialize the result string.
    i = 0  # Start index of a character group.
    j = 0  # Pointer for scanning through the string.

    while j < len(s):  # Traverse the string.
        if s[i] == s[j]:  # If the characters are the same, move j forward.
            j += 1
        else:  # A different character is found, meaning the previous character group ended.
            num = j - i  # Compute the length of the repeated sequence.

            if num == 1:  # If only one occurrence, just append the character.
                result += s[i]
            else:  # If more than one occurrence, append count followed by the character.
                result += str(num) + s[i]

            i = j  # Move i to the new character's position.

    return result  # Return the compressed string.

def compress_better(s):
    result = ""
    i = 0
    n = len(s)

    while i < n:
        j = i + 1 # Start of the current character sequence
        while j < n and s[i] == s[j]:  # Count occurrences
            j += 1
        
        count = j - i  # Compute frequency
        result += (str(count) + s[i]) if count > 1 else s[i]
        
        i = j  # Move to the next unique character

    return result

print(compress("aaabbc"))  # Output: "3a2bc"

test_cases = [
    "aabbbc",
    "oops",
    ""
]

for test in test_cases:
    print(f"Slower -> Input: {test} -> Output: {compress(test)}")
    
for test in test_cases:
    print(f"Slower -> Input: {test} -> Output: {compress_better(test)}")