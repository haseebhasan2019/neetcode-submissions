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
            curr_candidate = candidates[i]
            curr.append(curr_candidate)
            backtrack(i+1, curr_sum+curr_candidate)
            curr.pop()
            while i+1 < len(candidates) and candidates[i+1] == curr_candidate:
                i+=1
            backtrack(i+1, curr_sum)
        backtrack(0, 0)
        return sums

# 1 2 2 2 3
# target = 4
# [[2,2][1,3]]
