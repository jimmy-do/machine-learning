def uncompress(s):
    numbers = '0123456789'  # Set of valid digits
    result = ''  # Output string
    i = 0  # Start index of a number
    j = 0  # End index of a number

    while j < len(s):  # Iterate through the string
        if s[j] in numbers:  # If the character is a digit
            j += 1  # Move to the next character
        else:
            num = int(s[i:j])  # Convert the number substring to an integer
            result += s[j] * num  # Repeat the next character num times
            j += 1  # Move past the character
            i = j  # Update the start index for the next number

    return result  # Return the expanded string
