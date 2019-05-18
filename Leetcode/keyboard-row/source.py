class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alphabet = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]
        ans = []

        index = 0
        for word in words:
            for idx in range(3):
                if word[0].upper() in alphabet[idx]:
                    index = idx
                    break

            one_row = True
            for char in word:
                if char.upper() not in alphabet[index]:
                    one_row = False
                    break

            if one_row:
                ans.append(word)
        return ans
