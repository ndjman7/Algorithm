class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        odd_list = []
        even_list = []

        for a in A:
            if a % 2 == 0:
                even_list.append(a)
            else:
                odd_list.append(a)

        return even_list + odd_list
