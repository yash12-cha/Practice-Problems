# Brute Force Approach
def lowerBound(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] >= target:
            return i
    return n

arr = [2, 3, 7, 10, 11, 11, 25]
target = 9
ans = lowerBound(arr, target)

'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Optimal Approach

def lowerBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= target:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

arr = [2, 3, 7, 10, 11, 11, 25]
target = 9
ans = lowerBound(arr, target)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''