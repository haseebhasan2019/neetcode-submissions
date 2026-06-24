class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []
        nums.sort()
        
        def backtrack(i):
            if i == len(nums):
                subsets.append(curr.copy())
                return 
            curr_num = nums[i]
            curr.append(curr_num)
            backtrack(i+1)
            curr.pop()
            while i < len(nums) and nums[i] == curr_num:
                i+=1
            backtrack(i)
        backtrack(0)
        return subsets

# include - 
# exclude - 

# 1 1 2

# [], 1, 11, 112, 12, 2

# sort the input list