
# Brute Force Approach

'''
When Buying:cap does not change.

When Selling:cap decreases by 1 (indicating one transaction has been completed).
'''

def solve(indx, prices, buy, cap):
    # Base case: if we have processed all prices or have no transactions left
    if indx >= len(prices) or cap == 0:
        return 0
    
    if buy:
        # If we can buy, we have two choices:
        # 1. Buy the stock at the current price and move to the next index (noting the cost)
        # 2. Skip buying and move to the next index
        profit = max(-prices[indx] + solve(indx + 1, prices, False, cap), 
                        solve(indx + 1, prices, True, cap))
    else:
        # If we can sell, we have two choices:
        # 1. Sell the stock at the current price and move to the next index (noting the profit)
        # 2. Skip selling and move to the next index
        profit = max(prices[indx] + solve(indx + 1, prices, True, cap - 1), 
                        solve(indx + 1, prices, False, cap))
    
    return profit
def maxProfit(prices):
    # Set the maximum number of transactions allowed
    cap = 2
    # Start the recursive process from the first index, with the option to buy
    return solve(0, prices, True, cap)

prices = [3,3,5,0,0,3,1,4]
ans = maxProfit(prices)

'''
Time Complexity (TC): O(2^n), where n is the number of prices.
Space Complexity (SC): O(n) for the recursion stack.
'''

# Better Approach 1

def solve(indx, prices, buy, cap, dp):
    # Base case: if we have processed all prices or have no transactions left
    if indx >= len(prices) or cap == 0:
        return 0
    
    # Check if the result is already computed (memoization)
    if dp[indx][buy][cap] != -1:
        return dp[indx][buy][cap]
    
    if buy:
        # If we can buy, we have two choices:
        # 1. Buy the stock at the current price and move to the next index (noting the cost)
        # 2. Skip buying and move to the next index
        profit = max(-prices[indx] + solve(indx + 1, prices, False, cap, dp), 
                        solve(indx + 1, prices, True, cap, dp))
    else:
        # If we can sell, we have two choices:
        # 1. Sell the stock at the current price and move to the next index (noting the profit)
        # 2. Skip selling and move to the next index
        profit = max(prices[indx] + solve(indx + 1, prices, True, cap - 1, dp), 
                        solve(indx + 1, prices, False, cap, dp))
    
    # Store the computed result in the memoization table
    dp[indx][buy][cap] = profit
    return profit

def maxProfit(prices):
    # Set the maximum number of transactions allowed
    cap = 2
    # Initialize the memoization table with -1
    # dp[indx][buy][cap] where:
    # indx: current index in prices
    # buy: 0 if we can buy, 1 if we can sell
    # cap: remaining transactions allowed
    dp = [[[-1 for _ in range(cap + 1)] for _ in range(2)] for _ in range(len(prices))]
    # Start the recursive process from the first index, with the option to buy
    return solve(0, prices, True, cap, dp)

prices = [3,3,5,0,0,3,1,4]
ans = maxProfit(prices)

'''
Time Complexity: O(N×2×3) 

Reason: There are three nested loops that account for O(N×2×3) complexity.

Space Complexity: O(N×2×3)

Reason: We are using an external array of size ‘N×2×3’. Stack Space is eliminated.
'''

# Better Approach 2

def maxProfit(prices):
    n = len(prices)  # Number of days (length of prices list)
    
    # Initialize the DP table
    # dp[indx][buy][cap] where:
    # indx: current index in prices
    # buy: 0 if we can buy, 1 if we can sell
    # cap: remaining transactions allowed (1 or 2)
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
    
    # Fill the DP table in reverse order
    for indx in range(n - 1, -1, -1):  # Iterate from the last day to the first
        for buy in range(2):  # 0 for buy state, 1 for sell state
            for cap in range(1, 3):  # Transaction counts: 1 or 2
                if buy:
                    # If we can buy, we have two choices:
                    # 1. Buy the stock at the current price
                    # 2. Skip buying
                    dp[indx][buy][cap] = max(
                        -prices[indx] + dp[indx + 1][0][cap],  # Buy the stock
                        dp[indx + 1][1][cap]  # Skip buying
                    )
                else:
                    # If we can sell, we have two choices:
                    # 1. Sell the stock at the current price
                    # 2. Skip selling
                    dp[indx][buy][cap] = max(
                        prices[indx] + dp[indx + 1][1][cap - 1],  # Sell the stock
                        dp[indx + 1][0][cap]  # Skip selling
                    )
    
    # The maximum profit is found at the starting index with the option to buy and 2 transactions allowed
    return dp[0][0][2]

'''
Time Complexity: O(N×2×3)
Reason: There are three nested loops that account for O(N×2×3) complexity.

Space Complexity: O(N×2×3)
Reason: We are using an external array of size ‘N×2×3’. Stack Space is eliminated.
'''