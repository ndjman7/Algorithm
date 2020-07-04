class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        answer = 1
        value = 0
        for num in nums:
            value += num
            if value < 0 and answer < -value + 1:
                answer = -value + 1

        return answer
