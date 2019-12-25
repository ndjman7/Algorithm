class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_val = min(A)
        max_val = max(A)
        if max_val - min_val <= 2*K:
            return 0

        return max_val - min_val - 2*K
