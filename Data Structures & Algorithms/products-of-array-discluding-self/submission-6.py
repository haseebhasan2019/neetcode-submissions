class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create right cumulative product
        res = [1] * len(nums)
        r = [1] * len(nums)
        l = [1] * len(nums)
        for i in range(len(nums)-1):
            r[i+1] = nums[i] * r[i]

        # Create left cumulative product
        for i in range(len(nums)-1,0,-1):
            l[i-1] = nums[i] * l[i]

        # Create result array
        for i in range(len(nums)):
            res[i] = r[i] * l[i] 
        return res
# 1 2 3 4

# 1  1  2 6 
# 24 12 4 1

# moving forward start at index 1
# moving backward start at index len - 2
# (skip the last number)

# 24 12 8 6