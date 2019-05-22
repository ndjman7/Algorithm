class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        cache = [-1 for _ in range(len(cost))]

        def dp(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dp(i+1), dp(i+2))
            return cache[i]

        return dp(0)
