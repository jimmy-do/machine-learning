# factorial
#
# Write a function, factorial, that takes in a number n and returns the factorial of that number.
# The factorial of n is the product of all the positive numbers less than or equal to n.
# You must solve this recursively.

def factorial(n):
    if n == 1:
        return 1
    elif n < 1:
        exit(1)
    print(f"Multiplying{n}...")
    return n * factorial(n-1)


# def factorial_wrong(n):
#     if n == 1:
#         return 1
#     elif n < 1:
#         exit(1)
#     n *= n - 1  # Modifies `n`, but does not recurse correctly
#     return factorial_wrong(n)  # Now calls with a wrongly modified `n`

print(factorial(10))
# print(factorial_wrong(5))