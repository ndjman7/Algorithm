import collections
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if collections.Counter(target) == collections.Counter(arr):
            return True
        return False

