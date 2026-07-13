class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2])
            dp[i]+=cost[i]
        return min(dp[-1], dp[-2])


# [1,2,1,2,1,1,1]
#  4 5 3 3 2 1 1 

# [1,2,1,2,1,1,1]
#  1 2 2 4 3 4 4 min of last 2 spots