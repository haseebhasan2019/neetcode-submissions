class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find target_row
        l = 0
        r = len(matrix)-1 # number of rows
        target_row = 0
        while l <= r:
            m = (l+r) // 2
            if matrix[m][0] < target:
                target_row = max(target_row, m)
                l = m+1
            elif matrix[m][0] > target:
                r = m-1  
            else:
                return True          
        # find col
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            m = (l+r) // 2
            if matrix[target_row][m] < target:
                l = m+1
            elif matrix[target_row][m] > target:
                r = m-1
            else:
                return True
        return False