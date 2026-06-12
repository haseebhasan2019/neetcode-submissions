class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]
        while l <= r:
            m = (l+r) // 2
            minimum = min(minimum, nums[m])
            if nums[m] < nums[r]:
                r = m-1
            else:
                l = m+1
        return minimum