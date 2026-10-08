class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set() # Store visited coordinates
        rows = len(grid)
        cols = len(grid[0])
        DIRS = ((0,1),(0,-1),(1,0),(-1,0))

        def dfs(row, col):
            visited.add((row, col))
            nonlocal rows, cols
            perimeter = 4
            for dr, dc in DIRS:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    perimeter -= 1
                    if (new_row, new_col) not in visited:
                        perimeter += dfs(new_row, new_col)
            return perimeter



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)
        return 0


'''
perimeter for a 1 starts at 4,
for each connected 1, subtract 1 from curr per
don't explore if a square has already been visited



0 1 0
0 1 1
= 8

0 0 0
1 1 1
= 8

1 0 0
1 1 1
= 10

0 1 1
0 1 1
= 8

0 1 0
0 1 1
0 0 1
= 10

1 1 1 1
= 10

0 1 0
1 1 1
= 10

0 0 0
0 1 0
0 0 0
= 4

0 0 0
0 1 1
0 1 1
= 8

'''