class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = [
            [row, sum(soldiers)]
            for row, soldiers
            in enumerate(mat)
        ]
        sort_dic = sorted(dic, key=lambda x: x[1])
        sort_weak = [x[0] for x in sort_dic]
        return sort_weak[:k]

