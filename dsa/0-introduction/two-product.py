def pair_product_brute_force(numbers, target_product):
  for i in range(len(numbers)): 
    for j in range(i+1,(len(numbers))):
      if numbers[i] * numbers[j] == target_product:
        return i,j
    
def pair_product_dictionary(numbers, target_product):
    previous_nums={} # initialize ds: hashmap
    
    for index, value in enumerate(numbers): # traverse our ds
        complement = target_product / value # complement logic
        
        if complement in previous_nums: # if complement exists in our hashmap/dictionary,
            # we will return the matching indices
            return previous_nums[complement],index
        
        previous_nums[value] = index # opposite day! We are assigning the index to the value e.g { 5 : 0 }, { 16 : 1 }
        
    return ()


nums = [5, 16, 86, 4, 1]
target = 16
result = pair_product_brute_force(nums, target)
faster_result = pair_product_dictionary(nums, target)
print(result)
print(faster_result)
