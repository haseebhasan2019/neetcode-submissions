class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums)-1):
            left[i+1] = nums[i] * left[i]
        print(left)
        for i in range(len(nums)-1,0,-1):
            right[i-1] = nums[i] * right[i]
        print(right)
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        return nums


# 1.  2.  4.  6. 

# x.  1.  2.  8.  
# 48. 24. 6.  x. 

# 48  24  12  8