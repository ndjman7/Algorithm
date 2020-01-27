class Solution:
    def maximum69Number (self, num: int) -> int:

        max_number = num

        list_num = list(str(num))
        for index, digit in enumerate(list_num):
            if digit == '6':
                list_num[index] = '9'
                str_num = ''.join(list_num)
                if max_number < int(str_num):
                    max_number = int(str_num)
                    break
                list_num[index] = '6'

        return max_number

