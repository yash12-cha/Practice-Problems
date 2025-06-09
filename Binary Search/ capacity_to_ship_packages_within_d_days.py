# Brute Force Approach

def daysRequired(weights, capacity):
    """
    Calculates the number of days required to ship all packages
    using the given ship capacity.
    """
    days = 1                # Start with day 1
    current_load = 0        # Current day's total load

    for weight in weights:
        # If adding the current package exceeds capacity,
        # move it to the next day and reset load
        if current_load + weight > capacity:
            days += 1
            current_load = weight
        else:
            current_load += weight

    return days

def shipWithinDays(weights, days):
    """
    Finds the minimum ship capacity needed to deliver all packages
    within the given number of days using brute-force.
    """
    # Minimum possible capacity is the max single weight
    # Maximum possible capacity is the sum of all weights (1 day)
    for capacity in range(max(weights), sum(weights) + 1):
        # Calculate how many days are needed for this capacity
        if daysRequired(weights, capacity) <= days:
            # If it's within the allowed days, return the capacity
            return capacity

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
res = shipWithinDays(weights, days)

'''
✅ Time and Space Complexity
Time Complexity:

Outer loop (capacity from max(weights) to sum(weights)) → O(S - M)
where S = sum(weights), M = max(weights)

Inner loop: O(n) to simulate loading

Total: O((S - M) * n) → Inefficient for large inputs

Space Complexity:

O(1) → No extra space used except variables
'''

def daysRequired(weights, capacity):
    """
    Helper function to calculate how many days are required
    to ship all packages with the given ship capacity.
    """
    days = 1
    current_load = 0

    for weight in weights:
        if current_load + weight > capacity:
            # Exceeds capacity → allocate to next day
            days += 1
            current_load = weight
        else:
            # Add weight to current day's load
            current_load += weight

    return days

def shipWithinDays(weights, days):
    """
    Uses binary search to find the minimum ship capacity
    needed to ship all packages within the given number of days.
    """
    low = max(weights)          # Minimum possible capacity (largest single item)
    high = sum(weights)         # Maximum possible capacity (all in one day)

    while low <= high:
        mid = (low + high) // 2
        required_days = daysRequired(weights, mid)

        if required_days <= days:
            # Try to minimize capacity → search left
            high = mid - 1
        else:
            # Not enough capacity → search right
            low = mid + 1

    return low  # Lowest valid capacity that meets the day constraint

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
res = shipWithinDays(weights, days)

'''
✅ Time & Space Complexity
Time Complexity:
O(n * log(sum(weights) - max(weights)))
where n = number of packages.
log() is from binary search, and O(n) is for simulating shipping days.

Space Complexity:
O(1) — only uses constant extra space.
'''