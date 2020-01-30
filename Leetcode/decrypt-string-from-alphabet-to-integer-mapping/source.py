class Solution:
    def freqAlphabets(self, s: str) -> str:

        answer = ''
        index = 0
        change_int = 96

        while index < len(s):
            if index+2 < len(s) and s[index+2] == '#':
                answer += chr(int(s[index:index+2]) + change_int)
                index += 3
            else:
                answer += chr(int(s[index]) + change_int)
                index += 1

        return answer
