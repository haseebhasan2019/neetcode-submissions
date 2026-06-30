class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int) # (i, curr_sum) -> count
        def backtrack(i, curr_sum):
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            if i == len(nums):
                return 1 if curr_sum == target else 0
            # add
            cache[(i,curr_sum)] += backtrack(i+1, curr_sum + nums[i])
            # subtract
            cache[(i,curr_sum)] += backtrack(i+1, curr_sum - nums[i])
            return cache[(i,curr_sum)]
        
        return backtrack(0, 0)

# backtracking
# 2 possible paths - add or subtract
# if you reach the end and sum = target -> increment count
