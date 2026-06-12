class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max_pos = 1
        prev_min_neg = 1
        res = nums[0]
        for num in nums:
            prev_max_pos, prev_min_neg = (
                max(num, num*prev_max_pos, num*prev_min_neg), 
                min(num, num*prev_max_pos, num*prev_min_neg)
            )
            res = max(res, prev_max_pos)
        return res