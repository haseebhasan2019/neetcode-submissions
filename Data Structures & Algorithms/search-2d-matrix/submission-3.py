class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS - 1
        while l <= r:
            m = (l+r) // 2
            val = matrix[m // COLS][m % COLS]
            if val < target:
                l = m+1
            elif val > target:
                r = m-1  
            else:
                return True          
        return False