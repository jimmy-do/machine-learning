def fizz_buzz(n):
    result = []  # initialize ds
    for i in range(1, n + 1):  # traverse the function argument
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:  # if divisible by 3, make the element "fizz"
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)

    return result


print(fizz_buzz(15))