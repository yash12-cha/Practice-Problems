# Brute Force Approach

def maxScore(cardPoints, k):
    n = len(cardPoints)
    max_score = 0

    # Try every possible split between front and back picks
    for i in range(k + 1):
        # Compute sum of the first i cards
        start_sum = 0
        for idx in range(i):
            start_sum += cardPoints[idx]

        # Compute sum of the last (k - i) cards
        end_sum = 0
        count = k - i             # how many cards to take from the end
        start_index = n - count   # start index for end segment
        for idx in range(start_index, n):
            end_sum += cardPoints[idx]

        total = start_sum + end_sum
        # Update the maximum score seen so far
        if total > max_score:
            max_score = total

    return max_score

cardPoints = [1,2,3,4,5,6,1]
k = 3
ans = maxScore(cardPoints, k)

'''
📊 Time Complexity:
O(k²), For each i (0…k), we run two loops of lengths up to i and k–i → O(k + k) = O(k). Overall: O(k·k)

Space Complexity:	
O(1), Uses only fixed counters and accumulators—no extra structures proportional to input size .
'''

# Optimal Approach

def maxScore(cardPoints, k):
    n = len(cardPoints)
    left_sum = 0
    # Sum of the first k cards (initially taking all from the left)
    for i in range(k):
        left_sum += cardPoints[i]
        max_sum = left_sum  # Track the best score so far

    # Initialize right_sum as 0; right_ptr points just after the last card
    right_sum = 0
    right_ptr = n - 1

    # Slide: shift one card at a time from left side to right side
    for left_ptr in range(k - 1, -1, -1):
        # Remove one card from left part
        left_sum -= cardPoints[left_ptr]
        # Add one card from the end
        right_sum += cardPoints[right_ptr]
        right_ptr -= 1
        # Update max_sum with combined sum of k cards
        max_sum = max(max_sum, left_sum + right_sum)

    return max_sum

cardPoints = [1,2,3,4,5,6,1]
k = 3
ans = maxScore(cardPoints, k)

'''
⌛ Time Complexity: O(k)
The algorithm begins by computing the sum of the first k cards in O(k).

Then, in the sliding window loop, it performs exactly k iterations, each doing O(1) work: one subtraction, one addition, and one comparison.

Total time is proportional to 2·k, which simplifies to O(k).

🧠 Space Complexity: O(1)
Uses a constant number of variables (left_sum, right_sum, max_sum, right_ptr).

No additional data structures whose size depends on the input.

Hence, the space usage remains constant .
'''