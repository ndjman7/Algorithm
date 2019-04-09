class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = True
            else:
                return True
        return False
