from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        balloon_dict = Counter(text)

        return min(
            balloon_dict['b'],
            balloon_dict['a'],
            balloon_dict['l'] // 2,
            balloon_dict['o'] // 2,
            balloon_dict['n']
        )
