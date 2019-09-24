import heapq


def solve():
    size = int(input())
    hq = []
    answer = []
    for _ in range(size):
        num = int(input())

        if num == 0:
            if len(hq) == 0:
                answer.append(0)
            else:
                answer.append(heapq.heappop(hq)[1])
        else:
            heapq.heappush(hq, (-num, num))

    for ans in answer:
        print(ans)


solve()
