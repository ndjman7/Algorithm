class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        value = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if value != arr[i+1] - arr[i]:
                return False
        return True

