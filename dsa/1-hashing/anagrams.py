# Function to check if two strings are anagrams
def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

# Helper function to count character frequencies in a string
def char_count(s):
    count = {}  # Initialize an empty dictionary

    for char in s:
        # If character is not in dictionary, initialize its count to 0
        if char not in count:
            count[char] = 0
        
        # Increment the count of the character
        count[char] += 1

    return count  # Return the dictionary with character counts


print(char_count("listen"))
print(char_count("silent"))

# Example Usage
print(anagrams("listen", "silent"))  # True
print(anagrams("hello", "world"))    # False