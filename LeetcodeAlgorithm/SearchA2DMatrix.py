class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False

        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][n - 1] >= target:
                break
        for j in range(n):
            if matrix[i][j] == target:
                return True
        return False