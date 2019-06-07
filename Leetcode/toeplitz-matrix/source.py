class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        Y = len(matrix)
        X = len(matrix[0])
        for y in range(Y):
            for x in range(X):
                if y+1 >= Y or x+1 >= X:
                    continue
                if matrix[y][x] != matrix[y+1][x+1]:
                    return False
        return True
