class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, max_jump in enumerate(nums):
            for jump in range(1, max_jump+1):
                curr = i + jump
                if curr >= len(nums):
                    break
                if not dp[curr]:
                    dp[curr] = dp[i] + 1
                else:
                    dp[curr] = min(dp[curr], dp[i] + 1)
        return dp[-1]

# [2,4,1,1,1,1]
#  o x       x

# [4 2 3 1]
#  o     x

# [2 4 1 2 3 1]
#  o x       x

# [2 3 4 2 3 1]
#  o   x     x

# [2 2 3 5 3 1 1 1 1]
#  o x   x         x

# 2 2 3 5 3 1 1 1 1
# 0 1 1


# 5 3 1 1 1 1
# 0 1 1 1 1 1

# 2 3 1 1 1 1
# 0 1 1 2 2 3