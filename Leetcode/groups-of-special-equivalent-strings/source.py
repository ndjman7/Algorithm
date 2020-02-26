class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        def rebuild_string(s):
            e = []
            o = []
            for i in range(len(s)):
                if i % 2 == 0:
                    e.append(s[i])
                else:
                    o.append(s[i])

            e = sorted(e)
            o = sorted(o)
            string = ''.join(e) + ''.join(o)
            return string

        def delete_string(s):
            while True:
                try:
                    A.remove(s)
                except ValueError:
                    return

        for i in range(len(A)):
            A[i] = rebuild_string(A[i])

        answer = 0

        while True:

            if len(A) == 0:
                break
            a = A[0]
            delete_string(a)
            answer += 1

        return answer
