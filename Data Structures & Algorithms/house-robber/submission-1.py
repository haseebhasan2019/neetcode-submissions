class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [nums[1], nums[0]] # in, out
        for i in range(2, len(nums)):
            prev_in, prev_out = dp
            # in = num + prev num out
            dp[0] = nums[i] + prev_out
            # out = max (prev num in or out)
            dp[1] = max(prev_in, prev_out)

        return max(dp)
