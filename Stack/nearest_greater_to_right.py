# Brute Force Approach

def nearestGreaterToRight(arr):
    n = len(arr)
    res = [-1] * n    # Initialize result array with -1 (default when no greater element)

    # For each position i, search for the next greater element to its right
    for i in range(n):
        # Look at all elements after i
        for j in range(i + 1, n):
            # As soon as we find one larger, that's the "next"
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break     # Stop at the first greater, important for correctness

    return res


arr = [1, 3, 2, 4]
ans = nearestGreaterToRight(arr)

'''
Time Complexity: O(n^2)

Space Complexity: O(n)
'''

# Optimal Approach

from collections import deque

def nearestGreaterToRight(arr):
    n = len(arr)
    stack = deque()  # Will hold candidates for next greater
    ans = []

    # Traverse from rightmost to leftmost
    for i in range(n - 1, -1, -1):
        # Remove any stack values ≤ current, they can't be next greater
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack empty, no greater element to the right
        if not stack:
            ans.append(-1)
        else:
            # Top of stack is next greater element
            ans.append(stack[-1])

        # Push current for future comparisons
        stack.append(arr[i])

    # Reverse to match original order
    ans.reverse()
    return ans

arr = [1, 3, 2, 4]
ans = nearestGreaterToRight(arr)

'''
Time Complexity: O(n)

Space Complexity: O(n)
'''