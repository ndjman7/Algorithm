class Solution:
    def divisorGame(self, N: int) -> bool:

        d = {}
        return self.dp(N, d)

    def dp(self, N, d):
        if N not in d:
            d[N] = False
            if N > 1:
                for i in range(1, N):
                    if N%i == 0:
                        d[N] = not self.dp(N-i, d)
                        if d[N]:
                            break
        return d[N]
