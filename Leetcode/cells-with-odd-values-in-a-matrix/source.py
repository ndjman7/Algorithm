class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        array = []
        for y in range(n):
            x_array = []
            for x in range(m):
                x_array.append(0)
            array.append(x_array)

        for point in indices:
            Y = point[0]
            X = point[1]
            for y in range(n):
                array[y][X] += 1
            for x in range(m):
                array[Y][x] += 1

        answer = 0
        for y in range(n):
            for x in range(m):
                if array[y][x] % 2 == 1:
                    answer += 1

        return answer
