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
            while i < len(nums):
                if curr_sum + nums[i] > target:
                    return
                curr.append(nums[i])
                backtrack(i, curr_sum+nums[i])
                curr.pop()
                i+=1
        backtrack(0, 0)
        return sums