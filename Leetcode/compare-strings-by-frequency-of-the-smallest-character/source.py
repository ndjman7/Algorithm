class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        frequency_list = []

        def findsmallestchar(word):
            minChar = word[0]
            frequency = 1
            for char in word[1:len(word)]:
                if char == minChar:
                    frequency=frequency+1
                elif char < minChar:
                    minChar = char
                    frequency = 1
            return frequency

        for word in words:
            frequency_list.append(findsmallestchar(word))

        answer = []

        for q in queries:
            value = findsmallestchar(q)
            c = 0
            for f in frequency_list:
                if f > value:
                    c += 1
            answer.append(c)

        return answer
