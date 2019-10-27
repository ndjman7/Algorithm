class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = []
        non_decreasing = False

        for index in range(len(A)-1):
            answer.append(A[index]**2)
        answer.append(A[len(A)-1]**2)
        answer = sorted(answer)

        return answer
