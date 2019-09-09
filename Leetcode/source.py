class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True

        if word.isupper():
            return True

        if word.islower():
            return True

        first_char = word[0]

        if first_char.islower():
            return False

        for rest_word in word[1:]:
            if rest_word.isupper():
                return False

        return True
