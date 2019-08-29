class Solution:
    def longestPalindrome(self, s: str) -> int:

        answer = 0

        alphabet_dict = {}
        for c in s:
            if c not in alphabet_dict:
                alphabet_dict[c] = 1
            else:
                alphabet_dict[c] += 1

        is_odd_exists = False

        for key, value in alphabet_dict.items():
            if value % 2 == 0:
                answer += value
            else:
                is_odd_exists = True
                answer += value - 1

        if is_odd_exists:
            answer += 1
        return answer
