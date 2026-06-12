class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for num in nums:
            if num-1 not in nums:
                end = num
                while end+1 in nums:
                    end+=1
                maxLen = max(maxLen, end-num+1)
        return maxLen