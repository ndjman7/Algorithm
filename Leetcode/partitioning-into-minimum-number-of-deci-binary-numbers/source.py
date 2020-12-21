class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0
        for char in n:
            if answer < int(char):
                answer = int(char)

        return answer

