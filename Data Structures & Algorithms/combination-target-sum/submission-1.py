class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort(reverse=True)
        def dfs(i, curr_list, curr_sum):
            curr_list.sort()
            if curr_sum == target:
                if curr_list not in res:
                    res.append(curr_list)
                return
            if curr_sum > target:
                return
            while i < len(nums):
                dfs(i, curr_list+[nums[i]], curr_sum+nums[i])
                i+=1
        dfs(0, [], 0)
        return res