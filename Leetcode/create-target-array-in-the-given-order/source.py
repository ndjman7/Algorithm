class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = [
            -1 for _ in range(len(nums))
        ]

        for num, i in zip(nums, index):
            if answer[i] != -1:
                for n_i in reversed(range(i, len(nums)-1)):
                    answer[n_i+1] = answer[n_i]
            answer[i] = num

        return answer

