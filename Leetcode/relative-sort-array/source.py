class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        for a2 in arr2:
            for index, a1 in enumerate(arr1):
                if a1 == a2:
                    ans.append(a1)
                    arr1[index] = -1

        arr1 = sorted(arr1)

        for a in arr1:
            if a != -1:
                ans.append(a)
        return ans
