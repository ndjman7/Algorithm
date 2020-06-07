class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        left_set = set()
        right_set = set()
        for left, right in paths:
            left_set.add(left)
            right_set.add(right)
        return tuple(right_set - left_set)[0]

