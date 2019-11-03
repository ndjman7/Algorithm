class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        answer = 0
        sorted_heights = sorted(heights)

        for h, a in zip(heights, sorted_heights):
            if h ^ a != 0:
                answer += 1

        return answer
