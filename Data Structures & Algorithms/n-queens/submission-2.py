class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set() # (r+c)
        neg_diag = set() # (r-c)
        solutions = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                solutions.append(copy)
                return
            
            for col in range(n):
                if col in cols or (row+col) in pos_diag or (row-col) in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                board[row][col] = 'Q'

                backtrack(row+1)

                cols.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                board[row][col] = '.'

        backtrack(0)
        return solutions

