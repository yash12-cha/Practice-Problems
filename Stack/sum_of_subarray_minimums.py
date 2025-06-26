
def sumSubarrayMins(arr):
    MOD = int(1e9 + 7)  # Use large prime MOD to avoid overflow
    sum_ = 0  # Initialize the total sum of minimums

    # Iterate over all possible starting points of subarrays
    for i in range(len(arr)):
        min_ = arr[i]  # Start with the first element as the minimum

        # Iterate over all ending points starting from i
        for j in range(i, len(arr)):
            # Update the current minimum in the subarray [i...j]
            min_ = min(min_, arr[j])

            # Add the minimum of current subarray to the total sum
            sum_ += min_
            sum_ %= MOD  # Keep sum within MOD range

    return sum_

arr = [3,1,2,4]
ans = sumSubarrayMins(arr)

'''
Time Complexity: O(n^2)

Space Complexity: O(n)
'''

# Optimal Approach

# Helper function to find the index of the Previous Less Element (PLE) for each element
def prev_less_index(arr):
    n = len(arr)
    stack = []
    ans = [-1] * n  # Default: no smaller element to the left

    for i in range(n):
        # Maintain a monotonic increasing stack (indices)
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        # Top of the stack is index of the nearest smaller element to the left
        if stack:
            ans[i] = stack[-1]

        # Push current index to stack
        stack.append(i)

    return ans

# Helper function to find the index of the Next Less Element (NLE) for each element
def next_less_index(arr):
    n = len(arr)
    stack = []
    ans = [n] * n  # Default: no smaller element to the right

    for i in range(n - 1, -1, -1):
        # Maintain a monotonic increasing stack (indices)
        while stack and arr[stack[-1]] > arr[i]:  # strictly '>' to handle duplicates correctly
            stack.pop()

        # Top of the stack is index of the nearest smaller element to the right
        if stack:
            ans[i] = stack[-1]

        # Push current index to stack
        stack.append(i)

    return ans

# Main function to calculate the sum of minimums of all subarrays
def sumSubarrayMins(arr):
    MOD = int(1e9 + 7)
    n = len(arr)
    total = 0

    # Get the index of previous and next less elements for each element
    prev_less = prev_less_index(arr)
    next_less = next_less_index(arr)

    # Contribution of arr[i] = arr[i] * (count of subarrays where arr[i] is the minimum)
    for i in range(n):
        # Number of elements on the left where arr[i] is the minimum
        left = i - prev_less[i]
        # Number of elements on the right where arr[i] is the minimum
        right = next_less[i] - i

        # Total subarrays where arr[i] is the minimum = left * right
        total += (arr[i] * left * right) % MOD
        total %= MOD  # To avoid overflow

    return total

arr = [3,1,2,4]
ans = sumSubarrayMins(arr)

'''
Time Complexity: O(3 * N)

Space Complexity: O(2 * N)
'''