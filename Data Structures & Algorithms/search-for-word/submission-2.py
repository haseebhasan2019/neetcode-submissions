class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            temp = board[row][col]
            board[row][col] = ""

            down = dfs(row+1, col, i+1) if row+1 < len(board) and board[row+1][col] == word[i] else False
            up = dfs(row-1, col, i+1) if row-1 >= 0 and board[row-1][col] == word[i] else False
            right = dfs(row, col+1, i+1) if col+1 < len(board[0]) and board[row][col+1] == word[i] else False
            left = dfs(row, col-1, i+1) if col-1 >= 0 and board[row][col-1] == word[i] else False

            board[row][col] = temp
            return down or up or left or right
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 1) == True:
                        return True
        return False
