class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(int) # (i, curr_sum) -> count
        def backtrack(i, curr_sum):
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            if i == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            # add
            add_count = backtrack(i+1, curr_sum + nums[i])
            cache[(i,curr_sum)]+=add_count
            # subtract
            sub_count = backtrack(i+1, curr_sum - nums[i])
            cache[(i,curr_sum)]+=sub_count
            return add_count + sub_count
        
        return backtrack(0, 0)

# backtracking
# 2 possible paths - add or subtract
# if you reach the end and sum = target -> increment count
