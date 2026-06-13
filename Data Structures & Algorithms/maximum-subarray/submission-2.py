class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr_sum = float('-inf'), 0
        for num in nums:
            curr_sum = max(num, curr_sum+num)
            res = max(res, curr_sum)
        return res