class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        first = ""
        for s in strs[1:]:
            for b, c in zip(ans, s):
                if (b==c):
                    first += b
                else:
                    break
            ans = first
            first = ""
        return ans
