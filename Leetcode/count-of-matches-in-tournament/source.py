class Solution:
    def numberOfMatches(self, n: int) -> int:

        answer = 0
        while n > 1:
            match = n // 2
            advance = n % 2
            n = match + advance
            answer += match

        return answer

