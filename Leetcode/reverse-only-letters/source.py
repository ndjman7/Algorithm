class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alphabet = []
        etc = []
        for i, c in enumerate(S):
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                alphabet.append(c)
            else:
                etc.append([i, c])

        alphabet.reverse()
        for value in etc:
            alphabet.insert(value[0], value[1])

        return ''.join(alphabet)
