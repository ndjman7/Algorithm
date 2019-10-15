class Solution:
    def balancedStringSplit(self, s: str) -> int:

        l_num = 0
        r_num = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == 'L':
                l_num += 1
                i += 1
            elif s[i] == 'R':
                r_num += 1
                i += 1
            if l_num == r_num:
                res += 1
        return res

