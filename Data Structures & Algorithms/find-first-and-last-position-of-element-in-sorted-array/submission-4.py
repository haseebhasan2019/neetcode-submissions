from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target) # first index of target
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        r = bisect_right(nums, target) - 1 # last index of target + 1
        return [l, r]
