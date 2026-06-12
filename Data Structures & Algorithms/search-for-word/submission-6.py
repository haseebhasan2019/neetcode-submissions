class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0])
                or board[row][col] != word[i]):
                return False
            char = board[row][col]
            board[row][col] = ""
            found = False
            for r, c in [[0,1],[1,0],[-1,0],[0,-1]]:
                if search(row+r, col+c, i+1):
                    found = True
                    break
            board[row][col] = char
            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if search(row, col, 0):
                    return True
        return False
