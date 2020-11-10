class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(len(points)-1):
            first = points[i]
            second = points[i+1]
            f_x, f_y = first
            s_x, s_y = second
            m = max(abs(f_x - s_x), abs(f_y - s_y))
            answer += m

        return answer
