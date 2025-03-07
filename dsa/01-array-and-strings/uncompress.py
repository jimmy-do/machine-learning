def uncompress_slower(s):
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

def uncompress_faster(s):
    numbers = '0123456789'
    result = []
    i = 0
    j = 0

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j]*num)
            j += 1
            i = j
    
    return ''.join(result)

test_cases = [
    "3a2b4c",
    "1a1b1c",
    "4x3y2z",
    "10a",
    "2p5q1r",
    "12m3n",
    "1z",
    "5a10b2c",
    "",
]

for test in test_cases:
    print(f"Slower -> Input: {test} -> Output: {uncompress_slower(test)}")

for test in test_cases:
    print(f"Faster -> Input: {test} -> Output: {uncompress_faster(test)}")
