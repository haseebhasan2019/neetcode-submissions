class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, curr_list, curr_sum):
            if curr_sum == target:
                if curr_list not in res:
                    res.append(curr_list.copy())
                return
            while i < len(nums):
                if curr_sum + nums[i] > target:
                    break
                curr_list.append(nums[i])
                dfs(i, curr_list, curr_sum+nums[i])
                curr_list.pop()
                i+=1
        dfs(0, [], 0)
        return res