class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for i in range(1, int(n/2)+1):
            answer.append(i)
            answer.append(-i)

        if n % 2 != 0:
            answer.append(0)

        return answer
