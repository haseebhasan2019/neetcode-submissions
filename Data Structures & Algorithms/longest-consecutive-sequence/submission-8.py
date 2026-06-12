class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for num in nums:
            if num-1 not in s: #Start of sequence
                end = num + 1
                while end in s:
                    end+=1
                maxLen = max(maxLen, end-num)
        return maxLen