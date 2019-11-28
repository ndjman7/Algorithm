class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        answer = 0
        count = 0

        for c in S:
            if c == "(":
                if count >= 0:
                    count += 1

            if c == ")":
                if count <= 0:
                    answer += 1
                else:
                    count -= 1

        answer += count

        return answer
