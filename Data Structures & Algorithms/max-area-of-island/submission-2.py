class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] != 1:
                return 0
            area = 1
            grid[row][col] = 2
            for dr, dc in ((-1,0),(1,0),(0,1),(0,-1)):
                area += dfs(row+dr, col+dc)
            return area
    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:   
                    max_size = max(max_size, dfs(row, col))
        return max_size