class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ans = {n: 0 for n in range(1, N+1)}
        for truth in trust:
            a, b = truth
            ans[a] = -100
            ans[b] += 1
        for key, value in ans.items():
            if value == N-1:
                return key
        return -1

