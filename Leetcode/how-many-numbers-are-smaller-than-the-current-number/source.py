class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        answer = [0 for _ in range(len(nums))]

        for a in range(len(nums)-1):
            for b in range(a+1, len(nums)):
                if nums[a] > nums[b]:
                    answer[a] += 1
                elif nums[a] < nums[b]:
                    answer[b] += 1

        return answer
