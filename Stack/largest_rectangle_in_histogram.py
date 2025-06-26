# Brute Force Approach

def largestRectangleArea(heights):
    n = len(heights)
    max_area = 0  # Stores the maximum area found so far

    # Try every possible starting point of the rectangle
    for i in range(n):
        min_height = float('inf')  # Track the minimum height in the current range

        # Extend the rectangle to the right
        for j in range(i, n):
            # Update minimum height for the current subarray [i...j]
            min_height = min(min_height, heights[j])

            # Area = min height × width
            width = j - i + 1
            area = min_height * width

            # Update max area if current is larger
            max_area = max(max_area, area)

    return max_area

heights = [2,1,5,6,2,3]
ans = largestRectangleArea(heights)

# Optimal Approach

from collections import deque

# Function to find index of nearest smaller element to the left for each bar
def nearest_smaller_to_left(heights):
    result = []
    stack = deque()  # Each element: [height, index]

    for i in range(len(heights)):
        # Pop until we find a smaller element or stack becomes empty
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()

        # If stack is empty, no smaller element to the left
        if not stack:
            result.append(-1)
        else:
            # Top of the stack is the nearest smaller to the left
            result.append(stack[-1][1])

        # Push current element to stack
        stack.append([heights[i], i])

    return result

# Function to find index of nearest smaller element to the right for each bar
def nearest_smaller_to_right(heights):
    result = []
    stack = deque()  # Each element: [height, index]
    n = len(heights)

    for i in range(n - 1, -1, -1):
        # Pop until we find a smaller element or stack becomes empty
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()

        # If stack is empty, no smaller element to the right
        if not stack:
            result.append(n)
        else:
            # Top of the stack is the nearest smaller to the right
            result.append(stack[-1][1])

        # Push current element to stack
        stack.append([heights[i], i])

    return result[::-1]  # Reverse to match original order

# Function to calculate the largest rectangle area in a histogram
def largestRectangleArea(heights):
    nsl = nearest_smaller_to_left(heights)
    nsr = nearest_smaller_to_right(heights)
    max_area = 0

    for i in range(len(heights)):
        width = nsr[i] - nsl[i] - 1  # Width of rectangle for current bar
        area = heights[i] * width    # Area using current bar as height
        max_area = max(max_area, area)

    return max_area

heights = [2,1,5,6,2,3]
ans = largestRectangleArea(heights)

'''
Time & Space Complexity:

Time: O(N)
Each element is pushed and popped at most once in both NSL and NSR.

Space: O(N)
For stacks and result arrays.
'''