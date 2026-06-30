class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, curr_sum):
            count = 0
            if i == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            # add
            count += backtrack(i+1, curr_sum + nums[i])
            # subtract
            count += backtrack(i+1, curr_sum - nums[i])
            return count
        
        return backtrack(0, 0)

# backtracking
# 2 possible paths - add or subtract
# if you reach the end and sum = target -> increment count
