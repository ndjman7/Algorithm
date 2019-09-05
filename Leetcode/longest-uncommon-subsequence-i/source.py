class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == "" and b == "":
            return -1

        max_length = -1
        if a not in b:
            max_length = len(a)

        if b not in a:
            max_length = max(max_length, len(b))

        return max_length
