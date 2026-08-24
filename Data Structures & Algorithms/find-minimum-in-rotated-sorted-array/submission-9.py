class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        MIN = nums[0]
        while l <= r:
            m = (l+r) // 2
            if nums[m] <= nums[r]:
                MIN = min(MIN, nums[m])
                r = m - 1
            else:
                l = m + 1
        return MIN