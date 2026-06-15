class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(n//2):
            for col in range(row, n-row-1):
                top = matrix[row][col]
                right = matrix[col][n-row-1]
                bot = matrix[n-row-1][n-col-1]
                left = matrix[n-col-1][row]
                # top -> right
                matrix[col][n-row-1] = top
                # right -> bottom
                matrix[n-row-1][n-col-1] = right
                # bottom -> left
                matrix[n-col-1][row] = bot
                # left -> top
                matrix[row][col] = left