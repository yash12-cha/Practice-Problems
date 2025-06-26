# Brute Force Approach

def trap(arr):
    # Number of bar heights
    n = len(arr)
    
    # Initialize total water trapped
    waterTrapped = 0
    
    # Iterate through each position to calculate water above it
    for i in range(n):
        # Use two pointers to scan left and right from position i
        j = i
        
        # Find the maximum height to the left of i (including i)
        leftMax = 0
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        
        # Reset j for scanning the right
        j = i
        
        # Find the maximum height to the right of i (including i)
        rightMax = 0
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        
        # Water that can be trapped on top of bar i is determined
        # by the smaller of leftMax and rightMax, minus the bar height
        waterTrapped += min(leftMax, rightMax) - arr[i]
    
    return waterTrapped

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(height)

'''
Time Complexity: O(N*N) as for each index we are calculating leftMax and rightMax so it is a nested loop.

Space Complexity: O(1).
'''

# Another Approach

def trap(arr):
    # Number of bars
    n = len(arr)
    
    # Precompute highest bar to the left of each index
    left = [0] * n
    left[0] = arr[0]
    for i in range(1, n):
        # highest up to current: either previous left max or current height
        left[i] = max(left[i - 1], arr[i])
    
    # Precompute highest bar to the right of each index
    right = [0] * n
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        # highest from right: either next right max or current height
        right[i] = max(right[i + 1], arr[i])
    
    # Compute total trapped water
    waterTrapped = 0
    for i in range(n):
        # water at i is min(left[i], right[i]) minus current bar height
        waterTrapped += min(left[i], right[i]) - arr[i]
    
    return waterTrapped

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(height)

'''
Time Complexity: O(3*N) as we are traversing through the array only once. And O(2*N) for computing prefix and suffix array.

Space Complexity: O(N)+O(N) for prefix and suffix arrays.
'''

# Another Approach

def trap(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Precompute right max for each index
    right = [0] * n
    right[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    # Use one pass from left to right
    water = 0
    left_max = arr[0]  # initialize with first bar

    for i in range(n):
        # Update current left maximum
        left_max = max(left_max, arr[i])
        # Water trapped at i: limited by min(left_max, right[i])
        water += min(left_max, right[i]) - arr[i]

    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(height)

'''
Time Complexity: O(2*N) as we are traversing through the array only once. And O(N) for computing suffix array.

Space Complexity: O(N) for suffix array
'''

def trap(heights):
    # Initialize pointers and running maxima on both sides
    l, r = 0, len(heights) - 1
    l_max = r_max = 0
    total = 0

    # Process until pointers meet
    while l < r:
        # Move the pointer with the lower bar, since that's the limiting side
        if heights[l] <= heights[r]:
            # If current left bar is shorter than known left max, it holds water
            if heights[l] < l_max:
                total += l_max - heights[l]
            else:
                # Update left max if this bar is the new highest
                l_max = heights[l]
            l += 1  # Move from left inward
        else:
            # Same logic for the right side
            if heights[r] < r_max:
                total += r_max - heights[r]
            else:
                r_max = heights[r]
            r -= 1  # Move from right inward

    return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(height)

'''
Time Complexity: O(N) because we are using 2 pointer approach.

Space Complexity: O(1) because we are not using anything extra.
'''