class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for s_c in s:
            for t_c in t:
                if s_c == t_c:
                    t.remove(t_c)
                    break
        return t[0]
