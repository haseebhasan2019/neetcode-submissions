class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        # []
        # See if an element is the start of a subsequence
        for i, num in enumerate(nums):
            longest = max(longest, 1)
            curr_len = 1
            while (num + 1) in num_set:
                curr_len+=1
                num+=1
            longest = max(longest, curr_len)
        return longest

# 13 12 11 7 6 5 4 3 2 1
# 0 ...       n
# n * n = n^2

# n = len of array



# 6 + 1 = 7 -> 7 + 1 = 8 ? no 
# longest = 2

# 5 + 1 = 6 -> 6 + 1 -> 7 + 1 no
# longest = 3