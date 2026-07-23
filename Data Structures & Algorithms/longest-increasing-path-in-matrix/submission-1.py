import sys
sys.setrecursionlimit(10**6)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        LIP = [[0 for _ in range(cols)] for _ in range(rows)]
        result = 0

        def dfs(row, col) -> int:
            if LIP[row][col]:
                return LIP[row][col]
            
            max_path = 0
            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        matrix[new_row][new_col] > matrix[row][col]):
                    max_path = max(max_path, dfs(new_row, new_col))
            LIP[row][col] = 1 + max_path
            return LIP[row][col]

        for row in range(rows):
            for col in range(cols):
                if not LIP[row][col]:
                    result = max(result, dfs(row, col))
        return result

# dfs(0,0)
#     dfs(0,1) 
#         -> 1
#     -> 2
# dfs(1,0)
#     dfs(0,0)
#         -> 2
#     -> 3
# dfs(1,1)
#     dfs(1,0)
#         -> 3
#     dfs(0,1)
#         -> 1
#     -> 4

# 3 4
# 2 1

# 2 1
# - -

# 2 1
# 3 -

# 2 1
# 3 4

# idea: once you set a square's longest increasing path LIP, when
#     another path reaches that square you can append its LIP
#     -> Won't explore a square more than once

# - - -
# - - -
# - - -

# 1 - -
# - - -
# - - -

# 1 1 -
# - - -
# - - -

# 1 1 2
# - - 1
# - - -

# 1 1 2
# 3 2 1
# - - -

# 1 1 2
# 3 2 1
# 4 1 -

# 1 1 2
# 3 2 1
# 4 1 1