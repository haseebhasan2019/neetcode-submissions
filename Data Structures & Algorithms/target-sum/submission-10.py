class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # either add or subtract current num from running total
        cache = {}

        def backtrack(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            sub = backtrack(i+1, total - nums[i])
            add = backtrack(i+1, total + nums[i])
            cache[(i, total)] = sub + add
            return sub + add

        return backtrack(0,0)