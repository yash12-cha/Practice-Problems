# Brute Force Approach
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

nums = [1,3,5,6]
target = 2
ans = searchInsert(nums, target)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Optimal Approach

def searchInsert(nums, target):
    n = len(nums)  # size of the array
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if nums[mid] >= target:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

nums = [1,3,5,6]
target = 2
ans = searchInsert(nums, target)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''