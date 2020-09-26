class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        count = 0
        for i in range(length):
            # decrease case
            if nums[i] > nums[i+1]:
                count += 1
                if (
                    (i != 0 and nums[i-1] > nums[i+1]) and
                    (i != length -1 and nums[i] > nums[i+2])
                ):
                    return False
                # two count is out
                if count > 1:
                    return False
        return True
