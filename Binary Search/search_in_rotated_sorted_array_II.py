# Brute Force Approach
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False

nums = [2,5,6,0,0,1,2]
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
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        # If duplicates are at the ends, skip them
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        # Left Sorted
        elif nums[low] <= nums[mid]:
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
    return False

nums = [2,5,6,0,0,1,2]
target = 0
ans = search(nums, target)

'''
Time Complexity: O(logN) for the best and average case. O(N/2) for the worst case. Here, N = size of the given array.
Reason: In the best and average scenarios, the binary search algorithm is primarily utilized and hence the time complexity is O(logN). However, in the worst-case scenario, where all array elements are the same but not the target (e.g., given array = {3, 3, 3, 3, 3, 3, 3}), we continue to reduce the search space by adjusting the low and high pointers until they intersect. This worst-case situation incurs a time complexity of O(N/2).

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''