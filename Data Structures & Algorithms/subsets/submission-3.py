class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_subset = []
        subsets = []

        def backtrack(i):
            if i == len(nums):
                subsets.append(curr_subset.copy())
                return
            # include
            curr_subset.append(nums[i])
            backtrack(i+1)
            # exclude
            curr_subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return subsets
'''
for each integer, can either include or exclude it
recurse through the entire decision tree of include and exclude for each integer
2^n subsets
'''