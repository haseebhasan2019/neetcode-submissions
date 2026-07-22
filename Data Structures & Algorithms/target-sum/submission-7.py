class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            add = backtrack(i+1, curr_sum + nums[i])
            sub = backtrack(i+1, curr_sum - nums[i])
            memo[(i, curr_sum)] = add + sub
            return add + sub
        
        return backtrack(0, 0)

# bt(0, 0) = 3
#     bt(1, 2) -> 1
#     bt(1, 0) = 2
#         bt(2, 2) -> 1
#         bt(2, 0)
#             bt(3,2) -> 1
