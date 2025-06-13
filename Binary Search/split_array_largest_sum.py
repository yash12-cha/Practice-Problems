# Brute Force Approach

def countPartitions(nums, max_sum):
    partitions = 1  # Start with one partition
    sub_array_sum = 0  # Initialize the sum of the current subarray

    for i in range(len(nums)):
        # If adding the current number does not exceed max_sum
        if sub_array_sum + nums[i] <= max_sum:
            sub_array_sum += nums[i]  # Add to the current subarray sum
        else:
            # If it exceeds, we need a new partition
            partitions += 1
            sub_array_sum = nums[i]  # Start a new subarray with the current number

    return partitions  # Return the total number of partitions needed

def splitArray(nums, k):
    low = max(nums)  # The minimum possible largest sum is the largest single element
    high = sum(nums)  # The maximum possible largest sum is the sum of all elements

    # Perform a linear search from low to high to find the minimized largest sum
    for max_sum in range(low, high + 1):
        # Count how many partitions are needed for the current max_sum
        if countPartitions(nums, max_sum) <= k:
            return max_sum  # Return the first max_sum that allows k or fewer partitions

    return low  # Fallback return, should not reach here if inputs are valid

nums = [7,2,5,10,8]
k = 2
ans = splitArray(nums, k)

'''
Time Complexity: O(N * (sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are using a loop from max(arr) to sum(arr) to check all possible values of time. Inside the loop, we are calling the countPartitions() function for each number. Now, inside the countPartitions() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''

# Optimal Approach
def countPartitions(nums, max_sum):
    partitions = 1  # Start with one partition
    sub_array_sum = 0  # Initialize the sum of the current subarray

    for i in range(len(nums)):
        # If adding the current number does not exceed max_sum
        if sub_array_sum + nums[i] <= max_sum:
            sub_array_sum += nums[i]  # Add to the current subarray sum
        else:
            # If it exceeds, we need a new partition
            partitions += 1
            sub_array_sum = nums[i]  # Start a new subarray with the current number

    return partitions  # Return the total number of partitions needed

def splitArray(nums, k):
    low = max(nums)  # The minimum possible largest sum is the largest single element
    high = sum(nums)  # The maximum possible largest sum is the sum of all elements
    max_sum = low  # Initialize max_sum to the minimum possible largest sum

    # Perform binary search to find the minimized largest sum
    while low <= high:
        mid = (low + high) // 2  # Calculate the mid-point of the current range

        # Count how many partitions are needed for the current mid as max_sum
        if countPartitions(nums, mid) <= k:
            max_sum = mid  # Update max_sum if we can split into k or fewer partitions
            high = mid - 1  # Try for a smaller max_sum
        else:
            low = mid + 1  # Increase max_sum since we need more partitions

    return max_sum  # Return the minimized largest sum found

nums = [7,2,5,10,8]
k = 2
ans = splitArray(nums, k)

'''
Time Complexity: O(N * log(sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are applying binary search on [max(arr), sum(arr)]. Inside the loop, we are calling the countPartitions() function for the value of ‘mid’. Now, inside the countPartitions() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''