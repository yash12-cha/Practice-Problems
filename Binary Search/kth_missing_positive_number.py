# Brute Force Approach

def findKthPositive(arr, k):
    # Initialize a counter for missing numbers
    missing_count = 0
    current = 1  # Start checking from the first positive integer
    # Continue until we find the k-th missing number
    while True:
        if current not in arr:
            missing_count += 1  # Increment missing count if current is not in arr
        
        # If we have found the k-th missing number, return it
        if missing_count == k:
            return current
        
        current += 1  # Move to the next positive integer

arr = [2,3,4,7,11]
k = 5
ans = findKthPositive(arr, k)

'''
Time and Space Complexity:

Time Complexity: 
O(k.n), where n is the length of the array. In the worst case, we may need to check up to k missing integers, and for each check, we may need to scan the entire array.

Space Complexity: 
O(1), as we are using a constant amount of extra space.
'''

# Optimal Approach

def findKthPositive(arr, k):
    n = len(arr)
    
    lo, hi = 0, n - 1  # Initialize binary search bounds
    res = n + k  # Default result if kth missing is beyond the last element
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        # Calculate how many numbers are missing before arr[mid]
        # missing = arr[mid] - (mid + 1)
        # Explanation:
        # - arr[mid] gives the actual number at index mid
        # - (mid + 1) is the ideal number at that position if no number was missing
        missing = arr[mid] - (mid + 1)
        
        if missing < k:
            # If missing numbers before mid are fewer than k,
            # search right half to find kth missing number
            lo = mid + 1
        else:
            # If missing numbers before mid are >= k,
            # potential answer is before or at mid
            # Update result position accordingly
            res = mid + k
            hi = mid - 1
    
    return res


arr = [2,3,4,7,11]
k = 5
ans = findKthPositive(arr, k)

'''
Time Complexity (TC):
O(logn), where n is the length of arr.
This is because the solution uses binary search, halving the search space each iteration.

Space Complexity (SC):
O(1) constant space because only a fixed number of variables are used.
'''