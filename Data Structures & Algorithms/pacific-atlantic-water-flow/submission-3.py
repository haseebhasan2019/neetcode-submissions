class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic = [[False for _ in range(cols)] for _ in range(rows)]
        DIRECTIONS = ((0,1), (1,0), (0,-1), (-1,0))

        # Travel up-hill to see all squares that can reach pacific / atlantic
        def dfs(row, col, grid):
            grid[row][col] = True
            for dx, dy in DIRECTIONS:
                new_row = row + dx
                new_col = col + dy
                # Valid square to reach from here
                if 0 <= new_row < rows and 0 <= new_col < cols and heights[new_row][new_col] >= heights[row][col]:
                    # If not previously reached
                    if not grid[new_row][new_col]:
                        dfs(new_row, new_col, grid)

        # Fill in Pacific grid
        for col in range(cols):
            dfs(0, col, pacific)
        for row in range(1, rows):
            dfs(row, 0, pacific)

        # Fill in Atlantic grid
        for col in range(cols):
            dfs(rows-1, col, atlantic)
        for row in range(rows-1):
            dfs(row, cols-1, atlantic)
            
        # Add overlaps to result array
        result = []
        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])
        return result


'''
1 1
1 1
ALL of the above

1 1
1 0

For each space, need to explore all paths to the edges
create a pacific grid
create an atlantic grid
Once you explore a square can you mark it as either or True or False? - only can mark false if you've explored all its neighbors

'''