class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        curr_size = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] != 1:
                return
            nonlocal curr_size
            curr_size+=1
            grid[row][col] = 2
            for dr, dc in ((-1,0),(1,0),(0,1),(0,-1)):
                dfs(row+dr, col+dc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)   
                    max_size = max(max_size, curr_size)
                    curr_size = 0
        return max_size


# 1 0 0
# 0 1 1
# 0 0 0

# 2 0 0
# 0 2 2
# 2 2 2

# - keep track of the size of an island
# - after done recursing through an island see if its max