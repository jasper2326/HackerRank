'''search a 2-d matrix from left_bottom'''

class Solution:
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        x, y = m - 1, 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1
        return False