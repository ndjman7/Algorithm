class Solution:
    def countBits(self, num: int) -> List[int]:
        def count_bits(num):
            bits = []
            while num > 0:
                bits.append(num%2)
                num = int(num/2)
            return sum(bits)

        answer = []
        for value in range(num+1):
            answer.append(count_bits(value))

        return answer
