class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        value = 0
        answer = []
        for num in nums:
            value += num
            answer.append(value)

        return answer
