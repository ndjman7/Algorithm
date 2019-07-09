class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        def next_idx_func(s, e, o_e):
            for index in range(s, e):
                if A[index] % 2 == o_e:
                    return index
            return -1

        size = len(A)
        for idx in range(size):
            # odd
            if idx % 2 == 1:
                if A[idx] % 2 == 0:
                    next_idx = next_idx_func(idx+1, size, 1)
                    A[idx], A[next_idx] = A[next_idx], A[idx]
            # even
            else:
                if A[idx] % 2 == 1:
                    next_idx = next_idx_func(idx+1, size, 0)

                    A[idx], A[next_idx] = A[next_idx], A[idx]
        return A
