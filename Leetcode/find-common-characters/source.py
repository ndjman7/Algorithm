from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        answer = []
        l = []
        for a in A:
            l.append(Counter(a))

        C = l[0]
        for key, value in C.items():
            for _ in range(value):
                check = True

                for i in range(1, len(l)):
                    c = l[i]

                    if key in c:
                        if c[key] > 0:
                            c[key] -= 1
                        else:
                            check = False
                            break
                    else:
                        check = False
                        break

                if check:
                    answer.append(key)

        return answer
