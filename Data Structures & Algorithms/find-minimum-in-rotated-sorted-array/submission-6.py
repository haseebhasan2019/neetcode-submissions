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

# 1 2 3 4
# 6 1 2 3 4 5

# if mid < right: search left
# else: search right


# 1 2 3 4 5

# 5 1 2 3 4

# 3 4 5 1 2