class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        size = len(A[0])
        for y, a in enumerate(A):
            for x, b in enumerate(a):
                reverse_x = size-1-x
                if reverse_x >= x:
                    continue
                A[y][x], A[y][reverse_x] = A[y][reverse_x], A[y][x]

        for y, a in enumerate(A):
            for x, b in enumerate(a):
                A[y][x] = abs(b-1)

        return A
