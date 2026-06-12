class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            curr = 1
            if num-1 not in nums_set:
                while num+curr in nums_set:
                    curr+=1
            longest = max(longest, curr)
        return longest

# Store nums in set
# Iterate through nums
# If num-1 not in set -> start of a subsequence
# Keep iterating num++ and update longest

# 0 2 4

# 3 2 1