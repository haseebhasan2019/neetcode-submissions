class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # (i, holding) -> max profit
        def dfs(i, holding):
            # End of the array
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            # Skip or cooldown
            cooldown = dfs(i+1, holding)
            if holding:
                # Sell - optimize for only selling for positive
                sell = dfs(i+2, False) + prices[i]
                memo[(i, True)] = max(cooldown, sell)
                return memo[(i, True)]
            else:
                # Buy
                buy = dfs(i+1, True) - prices[i]
                memo[(i, False)] = max(cooldown, buy)
                return memo[(i, False)]
        return dfs(0, False)

        
# situations: 
# Cooldown - no choice - is ONLY one day after a sell
# have to buy - if we know we'll be able to sell for a profit
# sell - option if we have currently bought a stock AND profit is postive
# holding stock

# try all the possible options
# when we reach the end of the array, we compare the profit with max profit


# input = prices of the stock on each day
# output = max profit we can achieve
# constraints = once we sell a stock, we have to wait at least a day to buy again
# - we can buy an sell multiple times

# 1 2 3 4
# b.    s
# profit = 4-1 = 3

# 1 2 3 4 5 6 
# b.        s
# profit = 5
# - no better buy date ahead, so keep it

# 1 2 3 3 2 4
# b.  s   b s
# profit = 4
# when price < curr_max (best sell price), then we CAN sell the stock

# 1 6 6 5 30
# b s.  b s
# profit = 25+5 > 29