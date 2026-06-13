class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # row = text1, col = text2
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for t1 in range(len(text1)-1,-1,-1):
            for t2 in range(len(text2)-1,-1,-1):
                if text1[t1] == text2[t2]:
                    dp[t1][t2] = dp[t1+1][t2+1] + 1
                else:
                    dp[t1][t2] = max(dp[t1][t2+1], dp[t1+1][t2])
        return dp[0][0]