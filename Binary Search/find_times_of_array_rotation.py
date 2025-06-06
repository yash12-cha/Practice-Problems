# Brute Force Approach

def findKRotation(arr):
    min_ele = float('inf')
    min_ele_idx = 0
    for i in range(len(arr)):
        if arr[i] < min_ele:
            min_ele = arr[i]
            min_ele_idx = i
    return min_ele_idx

arr = [5, 1, 2, 3, 4]
ans = findKRotation(arr)

'''
Time Complexity: O(N), N = size of the given array.
Reason: We have to iterate through the entire array to check if the target is present in the array.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''

# Optimal Approach

def findKRotation(arr):
    low = 0
    high = len(arr) - 1
    ans = float('inf')
    index = -1
    while low <= high:
        mid = (low + high) // 2

        # If search space is already sorted,
        # then arr[low] will always be
        # the minimum in that search space
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            break

        # If left part is sorted
        if arr[low] <= arr[mid]:
            # Keep the minimum
            if arr[low] < ans:
                index = low
                ans = arr[low]

            # Eliminate left half
            low = mid + 1
        else:  # If right part is sorted
            # Keep the minimum
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]

            # Eliminate right half
            high = mid - 1

    return index
arr = [5, 1, 2, 3, 4]
ans = findKRotation(arr)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''