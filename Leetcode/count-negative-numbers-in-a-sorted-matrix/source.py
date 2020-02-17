class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0

        for line in grid:
            for column in line:
                if column < 0:
                    answer += 1

        return answer
