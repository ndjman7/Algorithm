from queue import Queue

def solve():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    size = int(input())
    board = [x[:] for x in [[0] * size] * size]
    visited = [x[:] for x in [[False] * size] * size]
    for y in range(size):
        line = input()
        for x, char in enumerate(line):
            board[y][x] = int(char)

    def bfs(input_y, input_x):
        q = Queue()
        q.put((input_y, input_x))
        visited[input_y][input_x] = True

        cnt = 1
        while not q.empty():
            y, x = q.get()

            for i in range(4):
                new_y = y + dy[i]
                new_x = x + dx[i]

                if new_y < 0 or new_y >= size:
                    continue
                if new_x < 0 or new_x >= size:
                    continue
                if visited[new_y][new_x]:
                    continue
                if board[new_y][new_x] == 0:
                    continue

                q.put((new_y, new_x))
                visited[new_y][new_x] = True
                cnt += 1

        return cnt

    cnt = 0
    answer_list = []
    for y in range(size):
        for x in range(size):
            if not visited[y][x] and board[y][x] == 1:
                answer_list.append(bfs(y, x))
                cnt += 1

    print(cnt)
    answer_list = sorted(answer_list)
    for answer in answer_list:
        print(answer)

if __name__ == '__main__':
    solve()
