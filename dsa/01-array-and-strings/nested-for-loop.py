def print_nested_chars(s):
    
    for char1 in s:  # Outer loop iterates over each character in s
        for char2 in s:  # Inner loop iterates over each character in s again
            print(char1 + ',' + char2)  # Prints all possible pairs of characters

    for char1 in s:  # Another loop iterating over s
        print(char1)  # Prints each character individually

print_nested_chars('qrs')  # Calling the function with the string 'qrs'