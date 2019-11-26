class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        import math
        p = label
        res = []
        while p >= 1:
            res.append(p)
            k = math.floor(math.log(p,2)) + 1
            p = int((3*math.pow(2,k-1) - 1 - p) / 2)
        res.reverse()
        return res
