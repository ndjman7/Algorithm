import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        answer = 0
        for key, value in counter.items():
            if value >= 2:
                for i in range(1, value):
                    answer += i

        return answer
