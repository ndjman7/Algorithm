class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Y = len(grid)
        X = len(grid[0])
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        ret = 0
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 0:
                    continue
                for d in range(4):
                    nextX = x + dx[d]
                    nextY = y + dy[d]
                    if nextY < 0 or nextX < 0 or nextY >= Y or nextX >= X:
                        ret += 1
                        continue

                    if grid[nextY][nextX] == 0:
                        ret += 1
        return ret
