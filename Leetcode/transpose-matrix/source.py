class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        for x in range(len(A[0])):
            l = []
            for y in range(len(A)):
                l.append(A[y][x])
            B.append(l)
        return B
