class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1, prev2 = 0, 0
        for i in range(len(nums)-1):
            num = nums[i]
            prev1, prev2 = max(num+prev2, prev1), prev1
        fwd = prev1
        prev1, prev2 = 0, 0
        for i in range(len(nums)-1,0,-1):
            num = nums[i]
            prev1, prev2 = max(num+prev2, prev1), prev1
        bwd = prev1
        return max(fwd, bwd)