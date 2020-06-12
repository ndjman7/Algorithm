class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        answer = []
        Y = len(matrix)
        X = len(matrix[0])
        def find_lucky_number(y, x):
            value = matrix[y][x]
            for i in range(X):
                if i == x:
                    continue
                if matrix[y][i] < value:
                    return

            for i in range(Y):
                if i == y:
                    continue
                if matrix[i][x] > value:
                    return
            answer.append(value)

        for y, row in enumerate(matrix):
            for x, element in enumerate(row):
                find_lucky_number(y, x)

        return answer
