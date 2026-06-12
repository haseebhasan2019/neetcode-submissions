class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for num in nums:
            start = end = num
            while start-1 in nums:
                start-=1
            while end+1 in nums:
                end+=1
            maxLen = max(maxLen, end-start+1)
        return maxLen