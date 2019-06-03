class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        color = image[sr][sc]
        import copy
        visited = copy.deepcopy(image)

        for y in range(len(visited)):
            for x in range(len(visited[0])):
                visited[y][x] = False

        def fill(y, x):
            visited[y][x] = True
            image[y][x] = newColor

            for i in range(4):
                newY = y + dy[i]
                newX = x + dx[i]

                if newY < 0 or newX < 0 or newY >= len(image) or newX >= len(image[0]):
                    continue

                if color != image[newY][newX]:
                    continue

                if visited[newY][newX]:
                    continue

                fill(newY, newX)

        fill(sr, sc)
        return image

