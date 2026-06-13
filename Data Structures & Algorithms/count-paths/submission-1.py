class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            col_grid = [1] * m
            for col in range(1, n):
                for row in range(1, m):
                    col_grid[row]+=col_grid[row-1]
            return col_grid[m-1]
        else:
            row_grid = [1] * n
            for col in range(1, m):
                for row in range(1, n):
                    row_grid[row]+=row_grid[row-1]
            return row_grid[n-1]
