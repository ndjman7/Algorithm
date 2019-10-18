class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        answer = []
        words = [word for word in text.split(' ')]

        for index, word in enumerate(words):
            if word == first:
                if index+1 < len(words)-1 and words[index+1] == second:
                    answer.append(words[index+2])

        return answer
