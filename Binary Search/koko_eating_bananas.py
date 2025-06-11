import math

# Brute Force Approach

def total_hours(speed, piles):
    
    # Calculate the total hours by summing the ceiling of each pile divided by speed
    # Since you cannot eat a fraction of a banana in an hour, you need to round up to the next whole hour
    return sum(math.ceil(pile / speed) for pile in piles)

def minEatingSpeed(piles, h):
    
    low, high = 1, max(piles)  # Set the range for the speed (1 to max pile size)
    result = high  # Initialize result to the maximum speed (worst case)

    # Iterate through each possible speed from low to high
    for speed in range(low, high + 1):
        total_hrs = total_hours(speed, piles)  # Calculate total hours at the current speed
        if total_hrs <= h:
            # If total hours is within the allowed hours, update the result
            result = min(speed, result)  # Keep the minimum valid speed

    return result  # Return the minimum speed found

piles = [3,6,7,11]
h = 8
ans = minEatingSpeed(piles,h)

'''
🕒 Time Complexity

-> Outer Loop: Iterates through all possible eating speeds from 1 to max(piles). Let m = max(piles). This results in O(m) iterations.
->Inner Computation: For each speed k, the total_hours function computes the total hours needed by iterating over all n piles, leading to O(n) operations per iteration.
-> Overall Time Complexity: Combining both, the total time complexity is O(n * m).
This can be inefficient, especially when max(piles) is large.

🧠 Space Complexity

-> Auxiliary Space: The algorithm uses a constant amount of extra space for variables like low, high, result, and loop counters.
-> Overall Space Complexity: O(1) (excluding the input list piles).
'''

# Optimal Approach

def total_hours(speed, piles):
    
    # Calculate the total hours by summing the ceiling of each pile divided by speed
    # Since you cannot eat a fraction of a banana in an hour, you need to round up to the next whole hour
    return sum(math.ceil(pile / speed) for pile in piles)

def minEatingSpeed(piles, h):
    low, high = 1, max(piles)  # Set the range for the speed (1 to max pile size)
    result = high  # Initialize result to the maximum speed (worst case)

    # Perform binary search on the range of speeds
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle speed
        hours = total_hours(mid, piles)  # Calculate total hours at the current speed

        if hours > h:
            # If total hours exceed allowed hours, we need to eat faster
            low = mid + 1  # Increase speed
        else:
            # If total hours are within the allowed hours
            result = mid  # Update result to the current mid speed
            high = mid - 1  # Try to find a slower speed that still works

    return result  # Return the minimum speed found

piles = [3,6,7,11]
h = 8
ans = minEatingSpeed(piles,h)

'''
🕒 Time Complexity

-> Binary Search Iterations: The binary search operates over the range of possible eating speeds, from 1 to max(piles). This results in O(log m) iterations, where m = max(piles).
-> Total Hours Calculation: For each candidate speed mid, the total_hours function computes the total hours needed by iterating over all n piles, leading to O(n) operations per iteration.
-> Overall Time Complexity: Combining both, the total time complexity is O(n * log m).
This is efficient and suitable for large datasets.

🧠 Space Complexity
-> Auxiliary Space: The algorithm uses a constant amount of extra space for variables like low, high, mid, and result.
-> Overall Space Complexity: O(1) (excluding the input list piles).
'''