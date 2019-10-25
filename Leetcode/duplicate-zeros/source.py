class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        for index in reversed(range(length-1)):
            if arr[index] == 0:
                for next_index in reversed(range(index+1, length)):
                    arr[next_index] = arr[next_index-1]

                arr[index+1] = 0
        return

