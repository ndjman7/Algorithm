class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        number_dict = {}
        for a in A:
            if a not in number_dict:
                number_dict[a] = 1
            else:
                return a
