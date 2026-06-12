class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            # Invalid
            if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0]) or 
                board[row][col] != word[i]):
                return False

            temp = board[row][col]
            board[row][col] = ""

            found = (dfs(row+1, col, i+1) or 
                dfs(row-1, col, i+1) or 
                dfs(row, col+1, i+1) or 
                dfs(row, col-1, i+1))

            board[row][col] = temp
            return found
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False
