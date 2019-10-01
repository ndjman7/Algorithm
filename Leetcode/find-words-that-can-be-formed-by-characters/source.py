class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        ans = 0
        char_dict = {}
        for char in chars:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        def find_word(word):
            import copy
            copy_dict = copy.deepcopy(char_dict)

            for char in word:
                try:
                    if copy_dict[char] <= 0:
                        return False
                    else:
                        copy_dict[char] -= 1
                except Exception:
                    return False

            return True

        for word in words:
            if find_word(word):
                ans += len(word)

        return ans
