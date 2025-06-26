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
        mid = (low + high) // 2  # Calculate the middle index
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return True
        
        # If duplicates are at the ends, skip them
        if nums[low] == nums[mid] == nums[high]:
            # When the elements at low, mid, and high are the same,
            # we cannot determine which side is sorted.
            # To avoid missing potential targets, we increment low
            # and decrement high to narrow down the search space.
            low += 1  # Move the low pointer to the right
            high -= 1  # Move the high pointer to the left
            
        # Left Sorted
        elif nums[low] <= nums[mid]:
            # If the left side is sorted
            if nums[low] <= target <= nums[mid]:
                # If the target is within the range of the sorted left side,
                # search in the left half by adjusting the high pointer.
                high = mid - 1
            else:
                # If the target is not in the range of the sorted left side,
                # search in the right half by adjusting the low pointer.
                low = mid + 1
        
        # Right Sorted
        else:
            # If the right side is sorted
            if nums[mid] <= target <= nums[high]:
                # If the target is within the range of the sorted right side,
                # search in the right half by adjusting the low pointer.
                low = mid + 1
            else:
                # If the target is not in the range of the sorted right side,
                # search in the left half by adjusting the high pointer.
                high = mid - 1
    
    # If we exit the loop, the target was not found
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