# Brute Force Approach

def searchRange(nums, target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]

nums = [5,7,7,8,8,10]
target = 8
ans = searchRange(nums, target)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Optimal Approach

def searchRange(nums, target):
    first = -1
    last = -1
    low = 0
    high = len(nums) - 1
    # Find the first occurrence of the target
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid  # Update first occurrence
            high = mid - 1  # Continue searching in the left half
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    # Reset low and high for the last occurrence search
    low = 0
    high = len(nums) - 1
    # Find the last occurrence of the target
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid  # Update last occurrence
            low = mid + 1  # Continue searching in the right half
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return [first, last]

nums = [5,7,7,8,8,10]
target = 8
ans = searchRange(nums, target)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''