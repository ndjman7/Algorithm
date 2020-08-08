class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = dict()
        for num in arr:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1

        max_value = -1
        for key, value in dic.items():
            if key == value:
                if max_value < key:
                    max_value = key

        return max_value
