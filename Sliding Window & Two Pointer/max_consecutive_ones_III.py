# Brute Force Approach

def longestOnes(nums, k):
    max_len = 0
    for i in range(len(nums)):
        zero_count = 0
        current_len = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zero_count += 1

            if zero_count > k:
                break
            current_len += 1
        max_len = max(max_len, current_len)  
    return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans = longestOnes(nums, k)

'''
Time Complexity:
O(n^2), because of the nested loops iterating over the array.

Space Complexity:
O(1), since only counters and variables are used.
'''

# Optimal Approach

def longestOnes(nums, k):
    left = 0  # Left pointer for the sliding window
    max_len = 0  # To store the maximum length of consecutive 1's found
    zero_count = 0  # To count the number of zeros in the current window
    for right in range(len(nums)):
        # If we encounter a zero, increment the zero count
        if nums[right] == 0:
            zero_count += 1
        
        # If the number of zeros exceeds k, shrink the window from the left
        if zero_count > k:
            if nums[left] == 0:
                zero_count -= 1  # Decrease the zero count
            left += 1  # Move the left pointer to the right
        
        # Update the maximum length of the window
        max_len = max(max_len, right - left + 1)
    return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans = longestOnes(nums, k)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''