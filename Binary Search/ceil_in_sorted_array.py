# Brute Force Approach
def findCeil(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] >= x:
            return i
    return -1

arr = [1, 2, 8, 10, 11, 12, 19]
x = 5
ans = findCeil(arr, x)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Optimal Approach

def findCeil(arr, x):
    ceil = -1
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] >= x:
            ceil = mid  # Update floor value
            high = mid - 1  # Search in the left half for a potentially smaller ceil
        else:
            low = mid + 1  # Search in the right half
    return ceil

arr = [1, 2, 8, 10, 11, 12, 19]
x = 5
ans = findCeil(arr, x)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''