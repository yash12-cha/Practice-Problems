# Brute Force Approach


def getTimeTaken(arr, max_pair_sum):
    num_painters = 1
    current_len = 0
    for length in arr:
        if current_len + length <= max_pair_sum:
            current_len += length
        else:
            num_painters += 1
            current_len = length
    return num_painters


def minTime(arr, k):
    min_time = sum(arr)
    for max_len_per_painter in range(max(arr), sum(arr) + 1):
        num_painters = getTimeTaken(arr, max_len_per_painter)
        if num_painters <= k:
            min_time = max_len_per_painter  # Update min_time if possible
            break  # Since we are iterating from smallest to largest, the first valid time is the minimum
    return min_time


# Example usage:
boards = [10, 20, 30, 40]
k = 2
ans = minTime(boards, k)

'''
Time Complexity: O(N * (sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are using a loop from max(arr) to sum(arr) to check all possible values of time. Inside the loop, we are calling the countPainters() function for each number. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''

# Optimal Approach


def getTimeTaken(arr, max_pair_sum):
    num_painters = 1  # Start with at least one painter
    current_len = (
        0  # Tracks the current total length of boards for the active painter
    )

    # Iterate through each board to assign it to a painter
    for length in arr:
        # If adding the current board doesn't exceed the max_pair_sum for the current painter
        if current_len + length <= max_pair_sum:
            current_len += (
                length  # Add the board to the current painter's work
            )
        else:
            # If adding the current board exceeds max_pair_sum, a new painter is needed
            num_painters += 1  # Increment the painter count
            current_len = length  # Assign the current board to the new painter

    return num_painters


def minTime(arr, k):
    # The search space for our answer (the minimum possible max_pair_sum)
    # The lower bound for the answer is the length of the longest single board,
    # as a painter must paint at least that much if it's the longest board.
    low = max(arr)

    # The upper bound for the answer is the sum of all board lengths,
    # which is the case if only one painter is available.
    high = sum(arr)

    # Initialize 'low' as the result; it will hold the optimal answer
    # once the binary search converges.
    # 'low' is used as the answer because when the loop terminates, 'low'
    # will be the smallest 'max_pair_sum' for which 'num_painters <= k'.
    ans = low

    # Perform binary search on the possible values of 'max_pair_sum'
    while low <= high:
        mid = (
            low + high
        ) // 2  # Calculate the middle value as a potential 'max_pair_sum'

        # Determine how many painters are needed if 'mid' is the maximum allowed length per painter
        num_painters = getTimeTaken(arr, mid)

        # If the number of painters required with 'mid' as the max_pair_sum is
        # less than or equal to 'k' (our available painters):
        # This 'mid' value might be a possible answer, or we might do even better
        # by trying a smaller 'max_pair_sum'.
        if num_painters <= k:
            ans = mid  # Store 'mid' as a potential answer
            high = (
                mid - 1
            )  # Try to find a smaller 'max_pair_sum' in the left half
        else:
            # If the number of painters required is greater than 'k':
            # 'mid' is too small; we need to increase the 'max_pair_sum' to reduce
            # the number of painters.
            low = (
                mid + 1
            )  # Search in the right half for a larger 'max_pair_sum'

    return ans  # The final 'low' (or 'ans') holds the minimum time


# Example usage:
boards = [10, 20, 30, 40]
k = 2
ans = minTime(boards, k)

'''
Time Complexity: O(N * log(sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are applying binary search on [max(arr), sum(arr)]. Inside the loop, we are calling the countPainters() function for the value of ‘mid’. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''