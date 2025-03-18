# sum numbers recursive
#
# Write a function sum_numbers_recursive that takes in an array of numbers and returns the sum of all
# the numbers in the array. All elements will be integers. Solve this recursively.

# def sum_numbers_recursive(numbers):
#     if len(numbers)==0:
#         return 0
#     return numbers[0] + sum_numbers_recursive(numbers[1:])
#
# print(sum_numbers_recursive([5, 2, 9, 10]))  # -> 26

def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        print("Base case reached: returning 0")
        return 0

    print(f"Calling sum_numbers_recursive({numbers[1:]}) - Adding {numbers[0]} later")
    result = numbers[0] + sum_numbers_recursive(numbers[1:])
    print(f"Returning {result} from sum_numbers_recursive({numbers})")
    return result

print("Final Result:", sum_numbers_recursive([5, 2, 9, 10]))
