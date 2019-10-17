class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        balloon_dict = {}
        answer = 0

        def input_dict(c):
            if c not in balloon_dict:
                balloon_dict[c] = 1
            else:
                balloon_dict[c] += 1
            return

        def check_ballon():
            if balloon_dict.get('b', 0) <= 0:
                return False
            balloon_dict['b'] -= 1

            if balloon_dict.get('a',  0) <= 0:
                return False
            balloon_dict['a'] -= 1

            if balloon_dict.get('l', 0) <= 1:
                return False
            balloon_dict['l'] -= 2

            if balloon_dict.get('o', 0) <= 1:
                return False
            balloon_dict['o'] -= 2

            if balloon_dict.get('n', 0) <= 0:
                return False
            balloon_dict['n'] -= 1

            return True

        for c in text:
            if c == 'b':
                input_dict(c)
            elif c == 'a':
                input_dict(c)
            elif c == 'l':
                input_dict(c)
            elif c == 'n':
                input_dict(c)
            elif c == 'o':
                input_dict(c)

        while True:
            if check_ballon():
                answer += 1
            else:
                break
        return answer
