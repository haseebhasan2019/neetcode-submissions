class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr_sum = 0
        count = 0

        def backtrack(i):
            nonlocal curr_sum, count
            if i == len(nums):
                if curr_sum == target:
                    count+=1
                return
            # add
            curr_sum+=nums[i]
            backtrack(i+1)
            curr_sum-=nums[i]
            # subtract
            curr_sum-=nums[i]
            backtrack(i+1)
            curr_sum+=nums[i]
        
        backtrack(0)
        return count

# backtracking
# 2 possible paths - add or subtract
# if you reach the end and sum = target -> increment count