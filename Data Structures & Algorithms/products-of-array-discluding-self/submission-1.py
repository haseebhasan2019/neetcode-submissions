class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = [0] * len(nums)
        b = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = nums[i] * f[i-1]
        b[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            b[i] = nums[i] * b[i+1]
        nums[0] = b[1]
        nums[-1] = f[-2]
        for i in range(1, len(nums)-1):
            nums[i] = f[i-1] * b[i+1]
        return nums

# 1 2 4 6

# 1  2  8  x
# 48 24 12 8
# x  48 24 6