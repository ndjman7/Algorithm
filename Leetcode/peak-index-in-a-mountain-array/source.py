class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        size = len(A)

        def binSearch(s, e):
            if s==e:
                return s

            m = int((s+e) / 2)

            if A[m] < A[m+1]:
                max_idx = binSearch(m+1, e)
            elif A[m] < A[m-1]:
                max_idx = binSearch(s, m-1)
            else:
                return m

            return max_idx

        return binSearch(0, size-1)

