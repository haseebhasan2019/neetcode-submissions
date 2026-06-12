class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_linear(nums):
            prev1, prev2 = 0, 0
            for num in nums:
                prev1, prev2 = max(num+prev2, prev1), prev1
            return prev1

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))