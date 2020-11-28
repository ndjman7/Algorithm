class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        Y = X = len(mat)

        check = [
            [False for _ in range(X)]
            for _
            in range(Y)
        ]

        answer = 0
        y = x = 0
        while True:
            if not check[y][x]:
                answer += mat[y][x]
                check[y][x] = True
            if y == Y-1 or x == X-1:
                break
            y += 1
            x += 1

        y = 0
        x = X - 1
        while True:
            if not check[y][x]:
                answer += mat[y][x]
                check[y][x] = True
            if y == Y-1:
                break
            y += 1
            x -= 1
        return answer
