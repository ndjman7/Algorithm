class Solution:
    def findComplement(self, num: int) -> int:

        two_bits = []
        while num != 0:
            two_bits.append(int(num % 2))
            num = int(num / 2)
        for i in range(len(two_bits)):
            if two_bits[i] == 0:
                two_bits[i] = 1
            else:
                two_bits[i] = 0
        answer = i = 0
        for num in two_bits:
            answer += int(num) * 2**i
            i += 1
        return answer
