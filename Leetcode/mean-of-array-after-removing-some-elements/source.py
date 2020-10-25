class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length = len(arr)
        count = int(length * 0.05)

        sorted_arr = sorted(arr)

        return sum(sorted_arr[count:length-count]) / (length-2*count)

