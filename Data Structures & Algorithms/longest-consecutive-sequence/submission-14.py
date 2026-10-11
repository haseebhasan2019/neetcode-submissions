class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for num in nums:
            # Start of a streak
            if num-1 not in nums_set:
                curr_streak = 1
                while num + curr_streak in nums_set:
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak                
                

