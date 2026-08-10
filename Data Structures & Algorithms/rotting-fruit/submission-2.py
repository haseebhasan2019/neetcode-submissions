class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # (minute, row, col)
        fruit = 0
        rotten = 0
        max_minute = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    if grid[row][col] == 2:
                        q.append((0, row, col))
                    fruit += 1
        
        while q:
            minute, row, col = q.popleft()
            rotten += 1
            max_minute = max(max_minute, minute)

            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and
                    grid[new_row][new_col] == 1):
                    # Mark fresh banana as rotten and enqueue
                    grid[new_row][new_col] = 2
                    q.append((minute + 1, new_row, new_col))

        return max_minute if fruit == rotten else -1


# Maintain a queue of the rotten fruits
# iterate through grid, count the total fruit, enq all rot
# enqueue all the neighbros who are fresh fruit
# keep going until the queue is empty
# if rotten fruit ct = fruit ct then return minutes else -1