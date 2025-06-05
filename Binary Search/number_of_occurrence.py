# Brute Force Approach
def countFreq(nums, target):
    n = len(nums)
    cnt = 0
    for i in range(n):
        if nums[i] == target:
            cnt += 1
    return cnt

arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
ans = countFreq(arr, target)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Another Approach
def countFreq(nums, target):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    if target in freq:
        return freq[target]
    else:
        return 0

arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
ans = countFreq(arr, target)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(N) as we are using hashmap for storing count
'''

# Optimal Approach

def countFreq(nums, target):
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
    if first == -1 or last == -1:  # If the element is not found
        return 0
    return last - first + 1

arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
ans = countFreq(arr, target)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''