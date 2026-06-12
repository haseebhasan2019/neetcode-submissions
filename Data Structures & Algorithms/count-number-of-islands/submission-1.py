class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
                grid[row][col] = "0"
                for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                    dfs(row+dr, col+dc)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count+=1
        return count