class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        curr = []
        nums = list(set(nums))
        nums.sort()

        def backtrack(i, curr_sum):
            if curr_sum == target:
                sums.append(curr.copy())
                return
            if curr_sum > target or i >= len(nums):
                return
            curr.append(nums[i])
            backtrack(i, curr_sum+nums[i])
            curr.pop()
            backtrack(i+1, curr_sum)

        backtrack(0, 0)
        return sums