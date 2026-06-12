class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minval = nums[0]

        while l <= r:
            if nums[r] > nums[l]:
                minval = min(minval, nums[l])
                break
            m = (l+r)//2
            minval = min(minval, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return minval
