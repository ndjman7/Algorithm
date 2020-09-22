class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        val = 0
        for a in A:
            if a % 2 == 0:
                val += a

        for index, query in enumerate(queries):

            query_index = query[1]
            if A[query_index] % 2:
                if query[0] % 2:
                    val += A[query_index] + query[0] else:
                if query[0] % 2 == 0:
                    val += query[0]
                else:
                    val -= A[query_index]

            A[query_index] += query[0]

            answer.append(val)

        return answer
