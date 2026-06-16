class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]
        return xor ^ len(nums)