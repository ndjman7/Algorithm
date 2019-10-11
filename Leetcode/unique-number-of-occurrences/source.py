class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1

        value_dict = {}
        for a in d.values():
            if a not in value_dict:
                value_dict[a] = 0
            else:
                return False

        return True
