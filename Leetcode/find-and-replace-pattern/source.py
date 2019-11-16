class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        answer = []
        for word in words:
            check = {}
            find = True
            for char, pa in zip(word, pattern):
                if pa not in check and char not in check.values():
                    check[pa] = char

                else:
                    if check.get(pa) != char:
                        find = False
                        break

            if find is True:
                answer.append(word)

        return answer
