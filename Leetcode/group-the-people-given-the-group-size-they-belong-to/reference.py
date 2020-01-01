class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        if not groupSizes:
            return []

        d = {}  # dict{int: List}
        for i in range(len(groupSizes)):
            key = groupSizes[i]

            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]

        out = [] # List[List[int]]
        for key, value in d.items():
            while value:
                arr = [] # List[int]
                for _ in range(key):
                    arr.append(value.pop())
                out.append(arr)
        return out
