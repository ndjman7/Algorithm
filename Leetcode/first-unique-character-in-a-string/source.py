import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(list(s))
        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
