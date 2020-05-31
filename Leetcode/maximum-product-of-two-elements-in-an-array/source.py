class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = 0
        max_index = 0
        for index, num in enumerate(nums):
            if max_value < num:
                max_value = num
                max_index = index

        answer = 0
        for index, num in enumerate(nums):
            if max_index == index:
                continue

            answer = max(answer, (num-1) * (max_value-1))
        return answer
