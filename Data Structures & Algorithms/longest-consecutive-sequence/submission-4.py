class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen = 0
        for num in nums:
            curr = 1
            if num-1 not in s: #start of an interval
                while num+1 in s:
                    curr+=1
                    num+=1
                maxlen = max(maxlen, curr)
        return maxlen

# Get the starts of each sequence search for num-1, then continue searching for num+1...
