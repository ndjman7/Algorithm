class Solution:
    def arrangeCoins(self, n: int) -> int:
        ret = 0
        k = 1
        while True:
            if n - k < 0:
                break
            n -= k
            k += 1
            ret += 1
        return ret
