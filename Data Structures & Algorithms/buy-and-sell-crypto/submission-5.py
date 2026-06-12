class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0 #min
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
                right+=1
            else:
                left = right
                right = left+1
        return max_profit
 
#  [10,1,5,6,7,1]

 
# buy price should always be the min
# sell should be the max