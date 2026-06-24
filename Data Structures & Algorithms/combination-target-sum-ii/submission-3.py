class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        curr = []
        candidates.sort()

        def backtrack(i, curr_sum):
            if curr_sum == target:
                combos.append(curr.copy())
                return
            if curr_sum > target or i == len(candidates):
                return
            # include - can have dups
            curr_num = candidates[i]
            curr.append(curr_num)
            backtrack(i+1, curr_sum+curr_num)
            # exclude - skip all dups
            curr.pop()
            while i < len(candidates) and candidates[i] == curr_num:
                i+=1
            backtrack(i, curr_sum)
        
        backtrack(0, 0)
        return combos