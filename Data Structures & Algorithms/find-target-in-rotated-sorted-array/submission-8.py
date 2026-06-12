class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # either the left or right side sorted
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]: #left side sorted
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1