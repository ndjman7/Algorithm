class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return_idx = 0
        for idx in range(len(nums)):
            if target <= nums[idx]:
                return_idx = idx
                break
        else:
            return_idx = len(nums)

        return return_idx
