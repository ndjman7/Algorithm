class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:


        nums = sorted(nums)

        answer = 0
        for num in nums[::2]:
            answer += num

        return answer
