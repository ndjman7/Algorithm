class Solution(object):
    nums = []
    cache = []

    def dp(self, i):
        if len(self.nums) <= i:
            return 0

        if self.cache[i] != -1:
            return self.cache[i]

        self.cache[i] = self.nums[i]
        value = max(self.dp(i+2), self.dp(i+3))
        self.cache[i] += value

        return self.cache[i]

    def rob(self, nums):
        nums = [0, 0] + nums
        self.nums = nums
        self.cache = [-1 for _ in range(len(nums))]
        self.dp(0)
        self.dp(1)
        value = max(0, self.cache[0], self.cache[1])

        return value
