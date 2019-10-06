class Solution:
    def reverseWords(self, s: str) -> str:

        if not s:
            return ''

        words = s.split(' ')

        answer = ''

        for word in words:
            answer += word[::-1]
            answer += ' '

        return answer.strip()
