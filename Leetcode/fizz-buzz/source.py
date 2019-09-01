class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        fizz = "Fizz"
        buzz = "Buzz"

        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append(fizz+buzz)
            elif i % 3 == 0:
                answer.append(fizz)
            elif i % 5 == 0:
                answer.append(buzz)
            else:
                answer.append(str(i))

        return answer
