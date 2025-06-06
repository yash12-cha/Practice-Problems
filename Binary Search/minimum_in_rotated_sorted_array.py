# Brute Force Approach
def findMin(nums):
    min_ele = float('inf')
    for i in range(len(nums)):
        if nums[i] < min_ele:
            min_ele = nums[i]
    return min_ele

nums = [3,4,5,1,2]
ans = findMin(nums)

'''
Time Complexity: O(N), N = size of the given array.
Reason: We have to iterate through the entire array to check if the target is present in the array.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''

# Optimal Approach
def findMin(nums):
    # Initialize min_ele to positive infinity to ensure any number in nums will be smaller
    min_ele = float('inf')
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # If the current subarray is already sorted
        if nums[low] <= nums[high]:
            # The smallest element is at the low index
            min_ele = min(min_ele, nums[low])
            break  # Since the subarray is sorted, we can exit the loop

        # If the left half is sorted
        if nums[low] <= nums[mid]:
            # The smallest element is either at low or in the right half
            min_ele = min(min_ele, nums[low])
            low = mid + 1  # Move to the right half
        else:
            # The right half is sorted, so the smallest element is at mid or in the left half
            min_ele = min(min_ele, nums[mid])
            high = mid - 1  # Move to the left half

    return min_ele

nums = [3,4,5,1,2]
ans = findMin(nums)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''