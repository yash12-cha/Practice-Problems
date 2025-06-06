# Brute Force Approach
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
ans = search(nums, target)

'''
Time Complexity: O(N), N = size of the given array.
Reason: We have to iterate through the entire array to check if the target is present in the array.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''

# Optimal Approach
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        # Left Sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right Sorted
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
ans = search(nums, target)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are using binary search to search the target.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''