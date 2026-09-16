class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or total + candidates[i] > target:
                return
            # include num
            curr.append(candidates[i])
            backtrack(i+1, total + candidates[i])
            curr.pop()

            # exclude num
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            backtrack(j, total)

        backtrack(0, 0)
        return res