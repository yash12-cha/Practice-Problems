# Brute Force Approach

def nearestGreaterToLeft(arr):
    n = len(arr)
    res = [-1] * n

    # For each element, scan leftwards to find first greater one
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break  # stop as soon as nearest greater is found

    return res

arr = [24, 11, 13, 21, 3]
ans = nearestGreaterToLeft(arr)

'''
Time Complexity: O(n^2)

Space Complexity: O(n)
'''

# Optimal Approach

from collections import deque

def nearestGreaterToLeft(arr):
    
    n = len(arr)
    stack = deque()
    ans = []

    # Traverse array from left to right
    for i in range(n):
        # Pop any values that are <= current, since they can't be nearest greater
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is empty, no greater value on the left
        if not stack:
            ans.append(-1)
        else:
            # Top of stack is nearest greater to the left
            ans.append(stack[-1])

        # Push current value as potential nearest greater for future elements
        stack.append(arr[i])

    return ans

arr = [24, 11, 13, 21, 3]
ans = nearestGreaterToLeft(arr)

'''
Time Complexity: O(n)

Space Complexity: O(n)
'''