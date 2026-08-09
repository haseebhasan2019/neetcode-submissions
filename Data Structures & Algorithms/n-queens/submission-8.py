class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]

        queens = []
        res = []

        def backtrack(row):
            # Solution found
            if row == n:
                sol = ["".join(row) for row in board]
                res.append(sol)
                return
            # Valid placement of queen
            for col in range(n):
                if (col not in cols and 
                    col-row not in neg_diag and
                    col+row not in pos_diag):
                    # Place queen, add exclusions, recurse forward
                    board[row][col] = 'Q'
                    cols.add(col)
                    pos_diag.add(col+row)
                    neg_diag.add(col-row)
                    backtrack(row+1)
                    # remove exclusions
                    board[row][col] = '.'
                    cols.remove(col)
                    pos_diag.remove(col+row)
                    neg_diag.remove(col-row)
        
        backtrack(0)
        return res



# . .
# . .

# Wherever you place, you need to exclude that row, column, and diagonal - there will be a positive and negative diagonal

# . . . .
# . . . .
# . . . .
# . . . .

# q - - -
# - - . .
# - . - .
# - . . -

# neg-diag
# 0,0 1,1 2,2 3,3... = c-r = 0
# 0,1 1,2 2,3 3,4... = c-r = 1
# 0,2 1,3 = c-r = 2
# 1,0 2,1 = c-r = -1

#  0  1  2  3
# -1  0  1  2
# -2 -1  0  1
# -3 -2 -1  0

# pos-diag
# 2,0 1,1 0,2 = c+r = 2
# 1,0 1,0 = c+r = 1

# 0 1 2 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6