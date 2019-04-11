class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, value in enumerate(nums):
            if value not in d:
                d[value] = index
            else:
                if k >= abs(index - d[value]):
                    return True
                d[value] = index
        return False
