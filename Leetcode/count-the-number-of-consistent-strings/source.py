class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        answer = 0

        allowed_dict = {}
        for key in allowed:
            allowed_dict[key] = True

        for word in words:

            is_consistent = True
            data = set(word)
            if len(data) > len(allowed):
                continue

            for key in word:
                if not allowed_dict.get(key):
                    is_consistent = False
                    break

            if is_consistent:
                answer += 1

        return answer
