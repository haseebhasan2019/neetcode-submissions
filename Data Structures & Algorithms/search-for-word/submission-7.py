class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or row >= len(board) or col < 0
                or col >= len(board[0]) or board[row][col] != word[i]):
                return False
            c = board[row][col]
            board[row][col] = ""
            for dr, dc in [[0,1],[0,-1],[-1,0],[1,0]]:
                if dfs(row+dr, col+dc, i+1):
                    return True
            board[row][col] = c
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False