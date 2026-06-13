class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_reach = 0
        for i in range(len(nums)):
            max_reach = max(max_reach, i+nums[i])
            if max_reach == i:
                return False
            if max_reach >= len(nums)-1:
                return True
        return False