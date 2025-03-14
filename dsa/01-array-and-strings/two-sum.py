def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices of the two numbers
    return []  # Return an empty list if no solution is found

def two_sum_dictionary(numbers, target_sum):
    previous_nums = {}  # Dictionary to store seen numbers and their indices

    for index, num in enumerate(numbers):
        complement = target_sum - num  # Compute required number to complete sum

        if complement in previous_nums:
            return (previous_nums[complement], index)  # Return matching indices

        previous_nums[num] = index  # Store current number with its index
        

# Example usage
nums = [3, 2, 5, 4, 1]
target = 8
result = two_sum_brute_force(nums, target)
faster_result = two_sum_dictionary(nums, target)
print(result)
print(faster_result)

