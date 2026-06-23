class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        prefix = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(prefix) == len(nums):
                permutations.append(prefix.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                prefix.append(nums[i])
                used[i] = True
                backtrack()
                prefix.pop()
                used[i] = False
            
        backtrack()
        return permutations

# need to keep track of a prefix to append to
# keep a set of the nums and those are the nums you need
# to choose from