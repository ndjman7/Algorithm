class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = ''
        address_list = address.split('.')
        for i in range(3):
            answer += address_list[i] + '[.]'
        answer += address_list[3]

        return answer
