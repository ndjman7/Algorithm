class Solution:
    def sortString(self, s: str) -> str:
        answer = []
        s_list = sorted(s)

        def find_smallest_or_largest_string(reverse=False):

            sort_s = sorted(s_list, reverse=reverse)
            data = []
            new_char = ''
            for i in range(len(sort_s)):
                if new_char != sort_s[i]:
                    new_char = sort_s[i]
                    data.append(new_char)

            for char in data:
                s_list.remove(char)

            nonlocal answer
            answer += data

        while True:
            if len(s_list) == 0:
                break
            find_smallest_or_largest_string(False)
            find_smallest_or_largest_string(True)

        return ''.join(answer)
