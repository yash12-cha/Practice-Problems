# Brute Force Approach

def nearestSmallerToRight(arr):
    n = len(arr)
    res = [-1] * n    # Initialize result array with -1 (default when no smaller element)

    # For each position i, search for the next smaller element to its right
    for i in range(n):
        # Look at all elements after i
        for j in range(i + 1, n):
            # As soon as we find one smaller, that's the "next"
            if arr[j] < arr[i]:
                res[i] = arr[j]
                break     # Stop at the first smaller, important for correctness

    return res


arr = [6, 4, 10, 2, 5]
ans = nearestSmallerToRight(arr)

'''
Time Complexity: O(n^2)

Space Complexity: O(n)
'''

# Optimal Approach

from collections import deque

def nearestSmallerToRight(arr):
    n = len(arr)
    stack = deque()  # Monotonic increasing stack to track future candidates
    ans = []

    # Traverse from rightmost to leftmost element
    for i in range(n - 1, -1, -1):
        # Pop items until a smaller candidate remains on top
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        # If stack is empty, no smaller element to the right
        if not stack:
            ans.append(-1)
        else:
            # Top of the stack is the nearest smaller to the right
            ans.append(stack[-1])

        # Push current value for future comparisons
        stack.append(arr[i])

    # Reverse result list to align with original array order
    ans.reverse()  
    return ans

arr = [6, 4, 10, 2, 5]
ans = nearestSmallerToRight(arr)

'''
Time Complexity: O(n)

Space Complexity: O(n)
'''