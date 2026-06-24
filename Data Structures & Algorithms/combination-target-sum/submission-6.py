class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        combos = []
        nums.sort()

        def backtrack(i, curr_sum):
            if curr_sum == target:
                combos.append(curr.copy())
                return
            if curr_sum > target or i == len(nums):
                return
            # include curr num
            curr.append(nums[i])
            backtrack(i, curr_sum+nums[i])
            # exclude curr num
            curr.pop()
            backtrack(i+1, curr_sum)
        
        backtrack(0,0)
        return combos