class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = maximum = 0
        s = set(nums)
        for num in nums:
            curr = 1
            if num-1 not in s:
                temp = num+1
                while temp in s:
                    curr+=1
                    temp+=1
            maximum = max(maximum, curr)
        return maximum
# start of a sequence = previous number not in set