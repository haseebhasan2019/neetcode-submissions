class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 1:
            return nums[0]
        dp = [[0 for _ in range(2)] for _ in range(houses)]
        dp[0] = [nums[0], 0] # in, out
        dp[1] = [nums[1], nums[0]]
        for i in range(2, houses):
            # in = num + prev num out
            dp[i][0] = nums[i] + dp[i-1][1] 
            # out = max (prev num in or out)
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])

        return max(dp[houses-1][0], dp[houses-1][1])
