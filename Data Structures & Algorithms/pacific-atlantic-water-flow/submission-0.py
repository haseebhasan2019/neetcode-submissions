class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(row, col, visited, prev):
            if (row < 0 or row >= rows or col < 0 or col >= cols or 
                heights[row][col] < prev or (row,col) in visited):
                return
            visited.add((row,col))
            for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                dfs(row+dr, col+dc, visited, heights[row][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
        for row in range(rows):
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        for col in range(cols):
            dfs(rows-1, col, atlantic, heights[rows-1][col])
        return [[row, col] for (row, col) in pacific & atlantic]