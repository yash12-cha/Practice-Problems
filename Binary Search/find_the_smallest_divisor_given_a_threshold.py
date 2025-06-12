import math

# Brute Force Approach
def smallestDivisor(nums, threshold):
    # Iterate through all possible divisors from 1 up to the maximum number in nums
    for divisor in range(1, max(nums) + 1):
        total = 0  # Initialize sum of divisions for this divisor
        # Calculate the sum of the ceiling of each division
        for num in nums:
            # ceil ensures that if there is any remainder in the division, it counts as an additional unit
            ele = math.ceil(num / divisor)  # Use ceil to round up division results
            total += ele
        # If the total sum of division results is within the allowed threshold,
        # return the current divisor as the smallest valid divisor
        if total <= threshold:
            return divisor
    # If no divisor satisfies the condition, return -1
    return -1

nums = [1,2,5,9]
threshold = 6
ans = smallestDivisor(nums, threshold)

'''
Time Complexity: O(max(arr)*N), where max(arr) = maximum element in the array, N = size of the array.
Reason: We are using nested loops. The outer loop runs from 1 to max(arr) and the inner loop runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''

def sumByD(nums, divisor):
    total_sum = 0
    for num in nums:
        # ceil ensures that if there is any remainder in the division, it counts as an additional unit
        ele = math.ceil(num / divisor) # Use ceil to round up division results
        total_sum += ele
    return total_sum

def smallestDivisor(nums, threshold):
    low = 1  # Minimum possible divisor
    high = max(nums)  # Maximum possible divisor (largest number in nums)
    # Binary search within the divisor range
    while low <= high:
        mid = (low + high) // 2  # Middle divisor to test
        # Calculate sum of divisions using mid as divisor
        if sumByD(nums, mid) <= threshold:
            # If sum is within threshold, try to find smaller divisor
            high = mid - 1
        else:
            # If sum exceeds threshold, increase divisor to decrease sum
            low = mid + 1
    return low # 'low' will be the smallest divisor satisfying the condition

nums = [1,2,5,9]
threshold = 6
ans = smallestDivisor(nums, threshold)


'''
Time Complexity: O(log(max(arr))*N), where max(arr) = maximum element in the array, N = size of the array.
Reason: We are applying binary search on our answers that are in the range of [1, max(arr)]. For every possible divisor ‘mid’, we call the sumByD() function. Inside that function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''