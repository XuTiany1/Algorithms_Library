def majority_element(nums):
    # Step 1: Find a candidate for the majority element
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    # Step 2: Verify if the candidate is indeed the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    if count > len(nums) // 2:
        return candidate
    else:
        return None

# Example usage
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(nums))  # Output: 4
