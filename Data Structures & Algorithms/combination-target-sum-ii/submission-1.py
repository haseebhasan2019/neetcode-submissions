class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = []
        curr = []
        candidates.sort()
        def backtrack(i, curr_sum):
            if curr_sum == target:
                sums.append(curr.copy())
                return
            if curr_sum > target or i >= len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                backtrack(j+1, curr_sum+candidates[j])
                curr.pop()
        backtrack(0, 0)
        return sums

# 1 2 2 2 3
# target = 4
# [[2,2][1,3]]
