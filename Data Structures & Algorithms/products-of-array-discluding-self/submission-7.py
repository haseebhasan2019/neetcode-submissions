class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # Iterate forward: Prefix product
        for i in range(len(nums)-1):
            res[i+1] = res[i] * nums[i]

        # Iterate backwards: Postfix product
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res