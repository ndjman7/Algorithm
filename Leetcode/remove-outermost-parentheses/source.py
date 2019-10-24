class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        pair = 0
        S = list(S)
        answer = ''
        for i in range(len(S)):
            if S[i] == '(':
                if pair == 0:
                    S[i] = 'X'
                pair += 1

            if S[i] == ')':
                if pair == 1:
                    S[i] = 'X'
                pair -= 1

        while True:
            try:
                S.remove('X')
            except ValueError:
                break

        for c in S:
            answer += c

        return answer
