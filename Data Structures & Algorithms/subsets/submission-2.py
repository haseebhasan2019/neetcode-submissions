class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                subsets.append(curr.copy())
                return
            # include current num
            curr.append(nums[i])
            backtrack(i+1)
            # exclude the current num
            curr.pop()
            backtrack(i+1)
        
        backtrack(0)
        return subsets

# 123
# 12
# 13
# 1
# 23
# 2
# 3
# []