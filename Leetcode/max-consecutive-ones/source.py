class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            max_num = max(max_num, cnt)
        return max_num
