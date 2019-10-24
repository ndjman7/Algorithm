class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        d = {"(": 1, ")": -1}
        i, s, r = 0, 0 ,''
        for idx, c in enumerate(S):
            s += d[c]
            if s == 0:
                r += S[i+1:idx]
                i = idx+1
        return r
