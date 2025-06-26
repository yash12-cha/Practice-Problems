# Brute Force Approach

def nearestSmallerToLeft(arr):
    n = len(arr)
    res = [-1] * n

    # For each element, scan leftwards to find first greater one
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                res[i] = arr[j]
                break  # stop as soon as nearest greater is found

    return res

arr = [6, 4, 10, 2, 5]
ans = nearestSmallerToLeft(arr)

'''
Time Complexity: O(n^2)

Space Complexity: O(n)
'''


# Optimal Approach

from collections import deque

def nearestSmallerToLeft(arr):
    
    n = len(arr)
    stack = deque()
    ans = []

    # Traverse array left to right
    for i in range(n):
        # Pop from stack while top is >= current element,
        # because those cannot be nearest smaller to the left for current or future values
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        # If stack is empty, no smaller element exists to the left
        if not stack:
            ans.append(-1)
        else:
            # Top of stack is the nearest smaller element to the left
            ans.append(stack[-1])

        # Push current element as potential candidate for future elements
        stack.append(arr[i])

    return ans

arr = [6, 4, 10, 2, 5]
ans = nearestSmallerToLeft(arr)

'''
Time Complexity: O(n)

Space Complexity: O(n)
'''