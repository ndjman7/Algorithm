class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = [0 for _ in range(26)]
        for s_c, t_c in zip(s, t):
            a[ord(s_c) - ord('a')] -= 1
            a[ord(t_c) - ord('a')] += 1

        if any(a):
            return False
        return True
