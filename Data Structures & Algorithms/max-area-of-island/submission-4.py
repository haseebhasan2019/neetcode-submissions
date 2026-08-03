class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(row, col):
            grid[row][col] = 2
            area = 1
            for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
                d_row = row + dr
                d_col = col + dc
                if (0 <= d_row < len(grid) and 0 <= d_col < len(grid[0]) and grid[d_row][d_col] == 1):
                    area += dfs(d_row, d_col)
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area