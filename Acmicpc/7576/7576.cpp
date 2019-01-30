#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > board;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int N, M, zero;
queue<pair<int, int> > q;

int tomato() {
    pair<int, int> p;
    int days = 0, size;

    while(true) {
        // 토마토가 더이상 존재하지 않는다면 break
        if(q.empty())
            break;

        size = q.size();

        while(size) {
            p = q.front();
            q.pop();
            for(int d = 0; d < 4; ++d) {
                int nextY = p.first + dy[d];
                int nextX = p.second + dx[d];
                if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= M)
                    continue;
                if(board[nextY][nextX] == 0) {
                    board[nextY][nextX] = -1;
                    zero--;
                    q.push(make_pair(nextY, nextX));
                }
            }
            size--;
        }
        days++;
    }
    // 0이 하나라도 존재하면 -1 반환
    if(zero)
        return -1;
    return days-1;
}

int main(void) {
    cin >> M >> N;
    board.resize(N, vector<int>(M));
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < M; ++x) {
            cin >> board[y][x];
            if(board[y][x] == 1) {
                q.push(make_pair(y, x));
                board[y][x] = -1;
            }
            if(board[y][x] == 0)
                zero++;
        }
    cout << tomato() << endl;
    return 0;
}
