class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_elevations = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        max_elevations[0][0] = grid[0][0]

        heap = []
        heapq.heappush(heap, (grid[0][0],0,0)) # (max elev so far, row, col)

        while heap:
            # pop min max elev from heap
            max_elev, row, col = heapq.heappop(heap)
            if row == rows-1 and col == cols-1:
                return max_elev
            # append valid neighbors
            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                new_row = row+dr
                new_col = col+dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_max_elev = max(grid[new_row][new_col], max_elev)
                    if new_max_elev < max_elevations[new_row][new_col]:
                        # update max_elevations
                        max_elevations[new_row][new_col] = new_max_elev
                        heapq.heappush(heap, (new_max_elev, new_row, new_col))

        return max_elevations[-1][-1]

# Initialization: dist of starting node = 0, all other nodes = infinity
# Edge relaxation (optimizing): look at the current node’s neighbors. 
    # Update their distance to the minimum of the newly calculated distance and their existing distance. 
# Node selection: mark the current node as visited. Select the node with the smallest distance and repeat step 2.
# Termination: algorithm completes when all nodes have been visited
