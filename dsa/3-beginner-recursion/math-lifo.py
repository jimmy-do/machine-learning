def multiply_by_2(x):
    print(f"multiply_by_2({x}) called")
    return x * 2

def add_3(y):
    print(f"add_3({y}) called")
    return multiply_by_2(y + 3)

def subtract_1(z):
    print(f"subtract_1({z}) called")
    return add_3(z - 1)

result = subtract_1(5)
print("Final result:", result)
