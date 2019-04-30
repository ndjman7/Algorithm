class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ans = dict()
        if len(pattern) != len(str.split(' ')):
            return False
        for p, s in zip(pattern, str.split(' ')):
            if p not in ans:
                if s in ans.values():
                    return False
                ans[p] = s
            else:
                if ans[p] != s:
                    return False
        return True
