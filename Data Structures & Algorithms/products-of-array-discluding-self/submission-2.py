class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = [0] * n
        b = [0] * n
        f[0] = b[-1] = 1
        for i in range(1, n):
            f[i] = nums[i-1] * f[i-1]
        for i in range(n-2, -1, -1):
            b[i] = nums[i+1] * b[i+1]
        for i in range(n):
            nums[i] = f[i] * b[i]
        return nums

# 1 2 4 6

# 1  1  2  8
# 48 24 12 8
# 48 24 6  1