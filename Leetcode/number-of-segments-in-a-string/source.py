class Solution:
    def countSegments(self, s: str) -> int:
        if s:
            words = s.split(' ')
            length = 0
            for word in words:
                if word:
                    length += 1
            return length
        return 0

