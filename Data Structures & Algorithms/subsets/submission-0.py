class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def backtrack(i, curr_set):
            if i == len(nums):
                subsets.append(curr_set.copy())
                return
            backtrack(i+1, curr_set)
            curr_set.append(nums[i])
            backtrack(i+1, curr_set)
            curr_set.pop()

        backtrack(0, [])
        return subsets


# for each number, we decide whether to add it to the set or not
# O(2^n)

# for each number we iterate through each other number
#  - two branches - include and exclude

# []
# 1
# 12
# 123
# 13
# 2
# 23
# 3
