class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(i, total):
            if total == target:
                res.append(curr[:])
                return
            if i == len(candidates) or candidates[i] + total > target:
                return
            # include current
            curr.append(candidates[i])
            backtrack(i+1, total + candidates[i])
            curr.pop()

            # exclude curr
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            backtrack(j, total)

        backtrack(0, 0)
        return res

# 1,2,2,4,5,6,9