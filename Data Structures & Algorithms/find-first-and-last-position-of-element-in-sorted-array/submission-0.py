class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums, target, True)
        right = self.binsearch(nums, target, False)
        return [left, right]
    
    def binsearch(self, nums: List[int], target: int, leftBias: bool) -> int:
        l = 0
        r = len(nums)-1
        res = -1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                res = m
                if leftBias:
                    r = m-1
                else:
                    l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return res

# Modifying binary search to have a left or right bias, call twice to get l and r