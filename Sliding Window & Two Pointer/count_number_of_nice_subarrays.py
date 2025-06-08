# Brute Force Approach
def numberOfSubarrays(nums, k):
    ans = 0
    for i in range(len(nums)):
        cnt_odd = 0

        for j in range(i, len(nums)):
            if nums[j] % 2 != 0:
                cnt_odd += 1

            # Check if we have exactly k odd numbers
            if cnt_odd == k:
                ans += 1

            # If we have more than k odd numbers, break the inner loop
            if cnt_odd > k:
                break
    return ans


nums = [1, 1, 2, 1, 1]
k = 3
ans = numberOfSubarrays(nums, k)

"""
🧠 Time and Space Complexity:
Time: O(n²) — nested loops for each starting index.

Space: O(1)
"""


# Optimal Approach
def atMostK(nums, k):
    left = 0
    count = 0
    current_odd = 0  # Tracks number of odd elements in current window

    for right in range(len(nums)):
        # If current element is odd, increment the count of odd numbers
        if nums[right] % 2 == 1:
            current_odd += 1

        # Shrink the window from the left if odd count exceeds k
        while current_odd > k:
            if nums[left] % 2 == 1:
                current_odd -= 1
            left += 1

        # All subarrays ending at 'right' and starting from 'left' to 'right' are valid
        count += right - left + 1

    return count


# Main function to get number of subarrays with exactly k odd numbers
def numberOfSubarrays(nums, k):
    return atMostK(nums, k) - atMostK(nums, k - 1)


nums = [1, 1, 2, 1, 1]
k = 3
ans = numberOfSubarrays(nums, k)

"""
🧠 Explanation Recap:
- atMostK(nums, k) gives all subarrays with at most k odd numbers
- atMostK(nums, k - 1) gives all subarrays with at most k - 1 odd numbers

We can calculate the number of subarrays with exactly k odd numbers, by subtracting:

All subarrays with at most k - 1 odd numbers
from
All subarrays with at most k odd numbers
"""

"""
🧠 Time Complexity:
O(n), Each element is visited at most twice: once by the right pointer and once by the left pointer in atMostK. Two calls to atMostK still keep it linear.
	
Space Complexity:
O(1), No extra space used apart from a few variables. No auxiliary data structures.
"""

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
