# Brute Force Approach
def upperBound(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] > target:
            return i
    return n

arr = [2, 3, 7, 10, 11, 11, 25]
target = 11
ans = upperBound(arr, target)


'''
Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''

# Optimal Approach

def upperBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1 # look on the right
        else:
            # maybe an answer
            ans = mid
            # look for smaller index on the left
            high = mid - 1

    return ans

arr = [2, 3, 7, 10, 11, 11, 25]
target = 11
ans = upperBound(arr, target)

'''
Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''