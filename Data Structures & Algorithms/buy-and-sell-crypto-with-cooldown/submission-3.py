class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # (i, holding) -> max profit
        def dfs(i, holding):
            # End of the array
            if i >= len(prices):
                return 0
            # This path is already cached
            if (i, holding) in memo:
                return memo[(i, holding)]
            # Skip or cooldown
            cooldown = dfs(i+1, holding)
            if holding:
                # Sell
                sell = dfs(i+2, not holding) + prices[i]
                memo[(i, holding)] = max(cooldown, sell)
            else:
                # Buy
                buy = dfs(i+1, not holding) - prices[i]
                memo[(i, holding)] = max(cooldown, buy)
            return memo[(i, holding)]
        return dfs(0, False)