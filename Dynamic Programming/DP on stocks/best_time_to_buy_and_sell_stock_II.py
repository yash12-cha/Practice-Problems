# Brute Force Approach

def solve(indx, prices, buy):
    # Base case: if index is out of bounds, return 0
    if indx >= len(prices):
        return 0
    
    if buy:
        # Max profit if we buy at current index or skip
        profit = max(-prices[indx] + solve(indx + 1, prices, False), 
                        solve(indx + 1, prices, True))
    else:
        # Max profit if we sell at current index or skip
        profit = max(prices[indx] + solve(indx + 1, prices, True), 
                        solve(indx + 1, prices, False))
    
    return profit
def maxProfit(prices):
    return solve(0, prices, True)

prices = [7,1,5,3,6,4]
ans = maxProfit(prices)

'''
Time Complexity (TC): O(2^n), where n is the number of prices.
Space Complexity (SC): O(n) for the recursion stack.
'''

# Better Approach 1

def solve(indx, prices, dp, buy):
    # Base case: no more days left
    if indx >= len(prices):
        return 0

    # If already computed, return the memoized result
    if dp[indx][buy] != -1:
        return dp[indx][buy]

    if buy:
        # Two choices: buy or skip
        profit = max(
            -prices[indx] + solve(indx + 1, prices, dp, 0),  # Buy
            solve(indx + 1, prices, dp, 1)                    # Skip
        )
    else:
        # Two choices: sell or skip
        profit = max(
            prices[indx] + solve(indx + 1, prices, dp, 1),   # Sell
            solve(indx + 1, prices, dp, 0)                   # Skip
        )

    # Memoize and return
    dp[indx][buy] = profit
    return profit

def maxProfit(prices):

    n = len(prices)
    # dp[i][buy]: max profit from index i onwards with buy state (1 for can buy, 0 for can sell)
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    return solve(0, prices, dp, 1)

prices = [7,1,5,3,6,4]
ans = maxProfit(prices)

'''
✅ Time Complexity (TC):
The function solve(indx, prices, dp, buy) has two parameters that affect state:

indx: ranges from 0 to n-1 → n possible values

buy: can be 0 or 1 → 2 possible values

So, the number of unique states is n * 2 = 2n

Each state is computed once due to memoization (dp[indx][buy]), and each computation takes constant time (just a couple of max calls and recursive calls).

👉 Total Time Complexity: O(n)

✅ Space Complexity (SC):
There are two components to space:

DP Table:

dp is a 2D list of size n x 2

So, space = O(n)

Recursive Call Stack:

At most n recursive calls on the call stack (in the worst case, you go all the way to indx = n)

So, space = O(n)

👉 Total Space Complexity: O(n)
'''

# Better Approach 2

def maxProfit(prices):
    n = len(prices)
    # dp[i][buy] = max profit starting from day i with state 'buy'
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]  # Extra row to handle base case (i == n)

    for i in range(n - 1, -1, -1):  # Iterate from last day to first
        for buy in range(2):  # 0 = we need to sell, 1 = we can buy
            if buy:
                # Option 1: Buy stock, Option 2: Skip
                dp[i][buy] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            else:
                # Option 1: Sell stock, Option 2: Skip
                dp[i][buy] = max(prices[i] + dp[i + 1][1], dp[i + 1][0])

    return dp[0][1]  # Start from day 0 with the option to buy

'''
✅ Time Complexity (TC):
You’re using a nested loop:

Outer loop: iterates i from n-1 to 0 → n iterations

Inner loop: iterates over buy = 0 and 1 → 2 iterations

Each cell dp[i][buy] is filled once with O(1) work.

👉 Total Time Complexity: O(n * 2) = O(n)

✅ Space Complexity (SC):
You're using a 2D DP table:

Size: dp[n+1][2] → (n+1 rows for days, 2 columns for buy state)

👉 Space Complexity: O(n * 2) = O(n)

Note: You can optimize space to O(2) (i.e., just two arrays curr[2] and next[2]) because the current day i only depends on i+1.
'''

# Optimal Approach

def maxProfit(prices):
    n = len(prices)

    # next_day[0] = max profit if we must sell (we already hold stock)
    # next_day[1] = max profit if we can buy
    next_day = [0, 0]  # Initialized to base case (after the last day)

    for i in range(n - 1, -1, -1):
        curr_day = [0, 0]
        # If we can buy
        curr_day[1] = max(-prices[i] + next_day[0], next_day[1])
        # If we can sell
        curr_day[0] = max(prices[i] + next_day[1], next_day[0])
        # Move to previous day
        next_day = curr_day

    return next_day[1]  # Start at day 0 with the option to buy

prices = [7,1,5,3,6,4]
ans = maxProfit(prices)

'''
✅ Time Complexity (TC):
You are using a single loop:

A single for loop runs from day n-1 to 0 → n iterations

In each iteration, you perform a few max and arithmetic operations → O(1) time per iteration

👉 Total Time Complexity: O(n)

✅ Space Complexity (SC):
Instead of maintaining a full n x 2 DP table, you're only using:

next_day[2] and curr_day[2]: fixed-size arrays

👉 Total Space Complexity: O(1) (constant space)
'''