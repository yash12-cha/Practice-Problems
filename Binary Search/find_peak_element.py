# Brute Force Approach

def findPeakElement(nums):
    n = len(nums)  # Get the length of the input list

    for i in range(n):
        # Check if the current element is greater than or equal to its left neighbor
        # For the first element, since there is no left neighbor, we consider this condition as True
        is_left_smaller = (i == 0) or (nums[i] >= nums[i - 1])

        # Check if the current element is greater than or equal to its right neighbor
        # For the last element, since there is no right neighbor, we consider this condition as True
        is_right_smaller = (i == n - 1) or (nums[i] >= nums[i + 1])

        # If both conditions are True, the current element is a peak
        if is_left_smaller and is_right_smaller:
            return i  # Return the index of the peak element

    # If no peak is found (which shouldn't happen for non-empty arrays), return -1
    return -1

nums = [1,2,3,1]
ans = findPeakElement(nums)

'''
Time Complexity: O(N), N = size of the given array.
Reason: We are traversing the entire array.

Space Complexity: O(1) as we are not using any extra space.
'''

# Optimal Approach
def findPeakElement(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Compare the middle element with its next neighbor
        if nums[mid] > nums[mid + 1]:
            # If the middle element is greater than its next neighbor,
            # then the peak lies on the left side (including mid)
            high = mid
        else:
            # If the middle element is less than or equal to its next neighbor,
            # then the peak lies on the right side (excluding mid)
            low = mid + 1

    # When low == high, we have found the peak element
    return low

nums = [1,2,3,1]
ans = findPeakElement(nums)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''