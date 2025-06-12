# Brute Force Approach 1

def mySqrt(x):
    ans = 0  # Initialize the answer variable to store the integer square root
    # Iterate from 1 to x to find the largest integer whose square is less than or equal to x
    for i in range(1, x + 1):
        val = i * i  # Calculate the square of the current integer i
        if val <= x:
            ans = i  # Update ans to the current integer i if its square is less than or equal to x
        else:
            break  # If the square exceeds x, exit the loop
    return ans  # Return the largest integer whose square is less than or equal to x

x = 4
ans = mySqrt(x)

'''
Time Complexity (TC):

The time complexity of this approach is O(x), where x is the input number. In the worst case, the loop runs x times to find the integer square root.

Space Complexity (SC):
The space complexity is O(1), as the function uses a constant amount of extra space regardless of the input size. The only variables used are ans and val.
'''

# Another Approach

import math

def mySqrt(x):
    ans = int(math.sqrt(x))
    return ans

x = 28
ans = mySqrt(x)

'''
Time Complexity: O(1)

Space Complexity: O(1) as we are not using any extra space.
'''

# Optimal Approach

def mySqrt(x):
    low = 0  # Start of the search range
    high = x  # End of the search range

    # Binary search to find the integer square root
    while low <= high:
        mid = (low + high) // 2  # Middle of the current search range
        val = mid * mid  # Square of mid

        if val <= x:
            # mid is a candidate; try for a larger value
            low = mid + 1
        else:
            # mid^2 is greater than x; discard upper half
            high = mid - 1

    # When the loop ends, high is the largest integer whose square is <= x
    return high

x = 28
ans = mySqrt(x)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are not using any extra space.
'''
