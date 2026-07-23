class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        memo = {}
        # either include or exclude the letter at i
        def backtrack(i, j):
            if j == len(t): # reach end of t -> valid subseq
                return 1
            if i == len(s): # reach end of s -> invalid subseq
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            ways = 0
            # include letter at i if equal to letter at j
            if s[i] == t[j]:
                ways += backtrack(i+1, j+1)
            # exclude letter at i if not
            ways += backtrack(i+1, j)
            memo[(i,j)] = ways
            return memo[(i,j)]
        
        return backtrack(0,0)