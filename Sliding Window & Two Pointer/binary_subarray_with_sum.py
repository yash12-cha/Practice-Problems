# Brute Force Approach
def numSubarraysWithSum(nums, goal):
    cnt = 0
    n = len(nums)

    # Iterate over all possible starting points of the subarray
    for i in range(n):
        current_sum = 0  # Reset current sum for each starting point
        # Iterate over all possible ending points of the subarray
        for j in range(i, n):
            current_sum += nums[
                j
            ]  # Add the current element to the current sum
            if current_sum == goal:  # Check if the current sum equals the goal
                cnt += 1  # Increment the count if it matches the goal

    return cnt


nums = [1, 0, 1, 0, 1]
goal = 2
ans = numSubarraysWithSum(nums, goal)

"""
🧠 Time and Space Complexity:
Time: O(n^2)
Space: O(1)
"""

# Optimal Approach
def numSubarraysWithSumLessThanGoal(nums, goal):
    if goal < 0:
        return 0  # No subarray can have a negative sum in binary array

    left = 0
    current_sum = 0
    count = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window if the current sum exceeds the goal
        while current_sum > goal:
            current_sum -= nums[left]
            left += 1

        # Count subarrays ending at 'right' with sum ≤ goal
        count += right - left + 1

    return count


def numSubarraysWithSum(nums, goal):
    return numSubarraysWithSumLessThanGoal(
        nums, goal
    ) - numSubarraysWithSumLessThanGoal(nums, goal - 1)

nums = [1, 0, 1, 0, 1]
goal = 2
ans = numSubarraysWithSum(nums, goal)
 
'''
🧠 Explanation Recap:
numSubarraysWithSumLessThanGoal counts how many subarrays have sum ≤ goal

Subtracting counts for goal and goal - 1 gives exactly those with sum == goal
'''

'''
⏱ Time Complexity:
Each element is processed at most twice: once by the right pointer, and once by the left pointer during shrinking.

So the total time is O(n), where n = len(nums).

💾 Space Complexity:
You're using only a few variables: left, right, current_sum, and count.

No extra data structures.

So the space is O(1).
'''

'''
🎯 Real-Life Example: Chocolate Bars 🍫
Let’s say you’re tracking how many chocolate bars kids eat in a day.

You want to know:

How many kids ate exactly 3 chocolate bars? (this is your k = 3)

✅ What’s Easy to Count?
It’s easy to count:

Kids who ate at most 3 chocolate bars
→ This includes kids who ate 0, 1, 2, and 3 bars
→ Suppose there are 50 kids like this.

Kids who ate at most 2 chocolate bars (k - 1)
→ This includes kids who ate 0, 1, or 2 bars
→ Suppose there are 30 kids like this.

🧠 Now Subtract:
If 50 kids ate at most 3, and 30 kids ate at most 2,
then only 20 kids ate exactly 3.

So:

Exactly k = At most k - At most (k - 1)
'''