class Solution:
    def binaryGap(self, N: int) -> int:
        binary = []
        while int(N / 2) > 0:
            binary.append(int(N % 2))
            N /= 2
        else:
            binary.append(int(N % 2))

        max_distance = distance = 0
        print(binary)
        start_index = binary.index(1)
        for num in binary[start_index:]:
            if num == 1:
                max_distance = max(max_distance, distance)
                distance = 0
            distance += 1

        return max_distance
