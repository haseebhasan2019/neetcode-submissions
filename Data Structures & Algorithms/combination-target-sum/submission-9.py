class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        curr_nums = []
        res = []

        def backtrack(i, total):
            if total == target:
                res.append(curr_nums.copy())
                return
            if i == len(nums) or nums[i] + total > target:
                return
            # include
            curr_nums.append(nums[i])
            backtrack(i, total + nums[i])
            curr_nums.pop()
            # exclude
            backtrack(i+1, total)
        
        backtrack(0,0)
        return res

