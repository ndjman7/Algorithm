class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        answer = 0
        val = 0
        length = len(nums)

        def find_long_length(index):
            nonlocal val
            val += 1
            if index == length -1:
                return
            if nums[index] < nums[index+1]:
                find_long_length(index+1)

        def find_all_long_length():
            nonlocal answer, val
            for index in range(len(nums)):
                find_long_length(index)
                answer = max(answer, val)
                val = 0

        find_all_long_length()

        return answer
