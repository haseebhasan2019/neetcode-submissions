class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ensure n is smaller than m for min space
        if m < n:
            m, n = n, m
        row_grid = [1] * n
        for _ in range(1, m):
            for col in range(1, n):
                row_grid[col]+=row_grid[col-1]
        return row_grid[-1]
