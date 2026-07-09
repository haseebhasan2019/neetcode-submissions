class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        while q:
            row, col, depth = q.popleft()
            grid[row][col] = min(grid[row][col], depth)
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if (0 <= row+dr < rows and 0 <= col+dc < cols and grid[dr+row][dc+col] > (depth+1)):
                    q.append((row+dr, col+dc, depth+1))


# ∞ -1  0  ∞
# ∞  ∞  ∞ -1
# ∞ -1  ∞ -1
# 0 -1  ∞  ∞

# 4 -1  0  1
# 3  2  1 -1
# 4 -1  2 -1
# 0 -1  3  4

# 3 -1  0  1
# 2  2  1 -1
# 1 -1  2 -1
# 0 -1  3  4