class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def backtrack(i, curr_sum):
            nonlocal count
            if i == len(nums):
                if curr_sum == target:
                    count+=1
                return
            # add
            backtrack(i+1, curr_sum + nums[i])
            # subtract
            backtrack(i+1, curr_sum - nums[i])
        
        backtrack(0, 0)
        return count

# backtracking
# 2 possible paths - add or subtract
# if you reach the end and sum = target -> increment count
