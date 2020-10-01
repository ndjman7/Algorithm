class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        length = len(grid)
        left_to_right = []
        top_to_bottom = []
        for i in range(length):
            max_value = -1
            for j in range(length):
                max_value = max(max_value, grid[i][j])
            top_to_bottom.append(max_value)

        for i in range(length):
            max_value = -1
            for j in range(length):
                max_value = max(max_value, grid[j][i])
            left_to_right.append(max_value)

        answer = 0
        for i in range(length):
            for j in range(length):
                value = grid[i][j]
                min_value = min(left_to_right[j], top_to_bottom[i])
                answer += min_value - value

        return answer
