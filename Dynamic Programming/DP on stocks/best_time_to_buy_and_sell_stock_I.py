
# Brute Force Approach

def maxProfit(prices):
    # Initialize maximum profit to 0
    max_profit = 0
    
    # Iterate through the list of prices
    for i in range(len(prices)):
        # Compare the current price with all subsequent prices
        for j in range(i + 1, len(prices)):
            # Calculate profit if selling at price[j] after buying at price[i]
            profit = prices[j] - prices[i]
            # Update max_profit if the current profit is greater
            max_profit = max(max_profit, profit)
    
    # Return the maximum profit found
    return max_profit

prices = [7,1,5,3,6,4]
ans = maxProfit(prices)

'''
Time Complexity (TC): O(n^2), where n is the number of prices, due to the nested loops.
Space Complexity (SC): O(1), as we are using a constant amount of space.
'''


# Optimal Approach

def maxProfit(prices):
    # Initialize maximum profit to 0
    max_profit = 0
    
    # Set the minimum price seen so far to the first price in the list
    min_so_far = prices[0]
    
    # Iterate through the list of prices starting from the second price
    for price in range(1, len(prices)):
        # Calculate profit if selling at the current price after buying at min_so_far
        profit = prices[price] - min_so_far
        
        # Update max_profit if the current profit is greater
        max_profit = max(max_profit, profit)
        
        # Update min_so_far to the minimum price seen so far
        min_so_far = min(min_so_far, prices[price])
    
    # Return the maximum profit found
    return max_profit

'''
Time Complexity (TC): O(n), where n is the number of prices, as we only traverse the list once.
Space Complexity (SC): O(1), as we are using a constant amount of space.
'''
