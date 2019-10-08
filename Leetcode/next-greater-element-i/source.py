class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for a in nums1:
            start_index = 1000
            find = False
            for index, b in enumerate(nums2):
                if a == b:
                    start_index = index

                if start_index < index:
                    if b > a:
                        ans.append(b)
                        find = True
                        break

            if find is False:
                ans.append(-1)

        return ans
