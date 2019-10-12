class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        table_mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        tableSum = [sum(table_mon[0:i+1]) for i in range(12)]
        table = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
        tmp = year - 1971
        tmp = tmp * 365 + int((tmp + 2) / 4)
        tmp += tableSum[month - 1]
        tmp += day
        if year != 2100 and (year % 4) == 0 and month > 2:
            tmp += 1
        tmp %= 7
        return table[tmp]

