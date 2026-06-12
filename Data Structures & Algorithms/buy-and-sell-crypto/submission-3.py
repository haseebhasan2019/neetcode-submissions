class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit, prices[i]-minBuy)
            minBuy = min(minBuy, prices[i])
        return maxProfit
