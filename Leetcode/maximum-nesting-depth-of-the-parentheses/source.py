class Solution:
    def maxDepth(self, s: str) -> int:
        s = list(s)
        m,cnt=0,0
        while s:
            temp = s.pop(0)
            if temp == "(":
                cnt+=1
            elif temp ==")":
                cnt-=1
            m = max(m,cnt)
        return m
