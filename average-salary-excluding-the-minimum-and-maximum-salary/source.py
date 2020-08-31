class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = 0
        min_salary = 100000000

        for i in salary:
            min_salary = min(i, min_salary)
            max_salary = max(i, max_salary)
        count = len(salary) - 2
        sum_salary = sum(salary) - (min_salary + max_salary)
        return sum_salary / count

