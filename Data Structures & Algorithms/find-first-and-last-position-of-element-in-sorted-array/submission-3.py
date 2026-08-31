from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = bisect_left(nums, target) # first index of target
        r = bisect_right(nums, target) - 1 # last index of target + 1
        if l < 0 or l >= len(nums) or r < 0 or r >= len(nums) or nums[l] != target or nums[r] != target:
            return [-1, -1]
        return [l, r]
