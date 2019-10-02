class Solution:
    def toGoatLatin(self, S: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = 1
        answer = ''

        for word in S.split(' '):
            if word[0] in vowels:
                word += 'ma'

            else:
                word = word[1:] + word[0] + 'ma'

            word += 'a' * a
            a += 1
            answer += word
            answer += ' '

        answer = answer.strip()

        return answer

