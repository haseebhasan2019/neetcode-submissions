class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        q = deque()

        def dfs(row, col):
            if board[row][col] == 's':
                return
            board[row][col] = 's'
            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                if (0 <= row+dr < rows and 0 <= col+dc < cols and board[row+dr][col+dc] == 'O'):
                    dfs(row+dr, col+dc)

        # Scan the edges and add all Os to a queue
        for row in range(rows):
            # first and last col
            if board[row][0] == 'O': q.append((row, 0))
            if board[row][cols-1] == 'O': q.append((row, cols-1))
        for col in range(1, cols-1):
            # top and bottom row
            if board[0][col] == 'O': q.append((0, col))
            if board[rows-1][col] == 'O': q.append((rows-1, col))
        # DFS all those space and change all connected Os to 's' to mark them safe
        while q:
            row, col = q.popleft()
            dfs(row, col)
        # Then iterate through the board and change all O -> X and s -> O
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 's':
                    board[row][col] = 'O'
