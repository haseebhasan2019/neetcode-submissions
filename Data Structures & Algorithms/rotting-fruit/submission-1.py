class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
        # bfs
        mins = 0
        while q:
            row, col, minute = q.popleft()
            mins = max(mins, minute)
            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                if (0 <= row+dr < rows and 0 <= col+dc < cols and grid[row+dr][col+dc] == 1):
                    grid[row+dr][col+dc] = 2
                    q.append((row+dr, col+dc, minute+1))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return mins

# minute 2
# [2,2,2,1,1,1,1,2,2,2]
# [2,2,2,1,1,1,1,2,2,2]
# [2 2 2 1,1,1,1,2 2 2]
# [1,1,1,1,1,1,1,1,1,1]
# [1,1,1,1,1,1,1,1,1,1]
# [1,1,1,1,1,1,1,1,1,1]
# [1,1,1,1,1,1,1,1,1,1]
# [2 2 2 1,1,1,1,2 2 2]
# [2,2,2,1,1,1,1,2,2,2]
# [2,2,2,1,1,1,1,2,2,2]

# # enqueue all rotting fruit (row, col, minute)
# # enqueue all its neighbors
# # Once queue is empty, search entire array for a fresh fruit - if exists, return -1, else mins