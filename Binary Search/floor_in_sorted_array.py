# Brute Force Approach

def findFloor(arr, x):
    ans = -1
    n = len(arr)
    for i in range(n):
        if arr[i] <= x:
            ans = i
    return ans

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
ans = findFloor(arr, x)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Optimal Approach

def findFloor(arr, x):
    floor = -1
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] <= x:
            floor = mid  # Update floor value
            low = mid + 1  # Search in the right half for a potentially larger floor
        else:
            high = mid - 1  # Search in the left half
    return floor

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
ans = findFloor(arr, x)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''