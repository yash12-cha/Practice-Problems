# Brute Force Approach

def canWePlace(stalls, dist, cows):
    
    countCows = 1  # Place the first cow in the first stall
    lastPosition = stalls[0]  # Track the last position where a cow was placed

    # Iterate through the stalls starting from the second stall
    for i in range(1, len(stalls)):
        # Check if the current stall is far enough from the last placed cow
        if stalls[i] - lastPosition >= dist:
            countCows += 1  # Place another cow
            lastPosition = stalls[i]  # Update the last position

    # Return True if we were able to place at least 'cows' cows
    return countCows >= cows

def aggressiveCows(stalls, k):
    stalls.sort()  # Sort the stall positions
    maxDist = stalls[-1] - stalls[0]  # Maximum possible distance between first and last stall

    # Initialize the best distance found
    bestDistance = 0

    # Check all possible distances from 1 to maxDist
    for dist in range(1, maxDist + 1):
        # If we can place cows with the current distance
        if canWePlace(stalls, dist, k):
            bestDistance = dist  # Update the best distance found

    return bestDistance  # Return the largest minimum distance found

stalls = [1, 2, 4, 8, 9]
k = 3
ans = aggressiveCows(stalls, k)

'''
Time Complexity (TC):
The time complexity of this brute force approach is O(n * d), where:
n is the number of stalls (length of stalls).
d is the maximum distance between the first and last stall (the range of distances checked).

Space Complexity (SC):
The space complexity is O(1), as the function uses a constant amount of extra space regardless of the input size. The variables used do not depend on the size of the input.
'''

# Optimal Approach

def canWePlace(stalls, dist, cows):
    countCows = 1  # Place the first cow in the first stall
    lastPosition = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - lastPosition >= dist:
            countCows += 1
            lastPosition = stalls[i]
            if countCows == cows:
                return True  # Successfully placed all cows
    return False  # Could not place all cows with given dist

def aggressiveCows(stalls, k):
    stalls.sort()
    low = 1  # Minimum possible distance
    high = stalls[-1] - stalls[0]  # Maximum possible distance
    best_dist = 0

    while low <= high:
        mid = (low + high) // 2
        if canWePlace(stalls, mid, k):
            best_dist = mid  # mid is a valid minimum distance
            low = mid + 1    # Try for a bigger distance
        else:
            high = mid - 1   # Try for a smaller distance

    return best_dist

stalls = [1, 2, 4, 8, 9]
k = 3
ans = aggressiveCows(stalls, k)

'''
Time Complexity: O(nlogd)
n = number of stalls
d = distance between the first and last stall (search space size for binary search)

Space Complexity: O(1)
'''