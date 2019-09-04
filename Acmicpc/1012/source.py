def solve():
    data = input().split(' ')
    input_y = int(data[0])
    input_x = int(data[1])
    size = int(data[2])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    answer = 0

    board = [x[:] for x in [[0] * input_x] * input_y]
    visited = [x[:] for x in [[False] * input_x] * input_y]

    for _ in range(size):
        data = input().split(' ')
        index_y = int(data[0])
        index_x = int(data[1])
        board[index_y][index_x] = 1

    def dfs(y, x):
        visited[y][x] = True
        board[y][x] = 0

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if new_y < 0 or input_y <= new_y:
                continue

            if new_x < 0 or input_x <= new_x:
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == 0:
                continue

            dfs(new_y, new_x)

    for y in range(input_y):
        for x in range(input_x):
            if board[y][x] == 1 and not visited[y][x]:
                dfs(y, x)
                answer += 1

    return answer

test_case = int(input())

for _ in range(test_case):
    print(solve())
