class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(curr_list, curr_sum, i):
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            while i < len(nums):
                if curr_sum + nums[i] > target:
                    return
                curr_list.append(nums[i])
                backtrack(curr_list, curr_sum+nums[i], i)
                curr_list.pop()
                i+=1
        backtrack([], 0, 0)
        return res