class Solution:
    def printMatrix(self, matrix):
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result


    def turn(self, matrix):
        row, col = len(matrix), len(matrix[0])
        newMat = []
        for i in range(col - 1, -1, -1):
            currentRow = []
            for j in range(row):
                currentRow.append(matrix[j][i])
            newMat.append(currentRow)
        return newMat

    def __init__(self, matrix):
        self.matrix = matrix


a = Solution(matrix=[[1, 2],
                     [4, 5]])
print(a.printMatrix([[1, 2],
                     [4, 5]]))