class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # no duplicates in each of these:
        # rows - keep a set for each row, reset at the end of the row
        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if board[row][col] in row_set:
                    return False
                row_set.add(board[row][col])
        # cols - same as above
        for col in range(len(board[0])):
            col_set = set()
            for row in range(len(board)):
                if board[row][col] == '.':
                    continue
                if board[row][col] in col_set:
                    return False
                col_set.add(board[row][col])
        # boxes - 3 boxes at a time: 0-147, 1-258, 2-369
        box_rows = 0
        boxes = defaultdict(set)
        for row in range(len(board)):
            if row // 3 > box_rows:
                boxes[0] = set()
                boxes[1] = set()
                boxes[2] = set()
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if board[row][col] in boxes[col // 3]:
                    return False
                boxes[col // 3].add(board[row][col])
        return True



# 1 2 3
# 4 5 6
# 7 8 9

# row // 3 + col // 3

# 0,0 -> 2,2 = 0
# 3,3 -> 5,5 = 2
# 6,6 -> 8,8 = 4

# if col // 3
# Iterate through the board
# if row // 3 > box_row (starts at 0) -> reset the box_sets
