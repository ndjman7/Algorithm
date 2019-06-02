class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        zero = False
        one = False
        for bit in bits[:-1]:
            if bit == 1 and one is False:
                one = True

            elif bit == 1 and one is True:
                one = False

            elif bit == 0 and one is True:
                one = False

        if one is True:
            return False
        return True
