#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N;
vector<vector<char> > board;
vector<vector<bool> > visited;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int y, int x, bool mang) {
    visited[y][x] = true;
    char color = board[y][x];
    queue<pair<int, int> > q;
    pair<int, int> p = make_pair(y, x);
    q.push(p);

    while(!q.empty()) {
        p = q.front();
        q.pop();

        for(int i = 0; i < 4; ++i) {
            int nextY = p.first + dy[i];
            int nextX = p.second + dx[i];

            if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= N) continue;

            if(visited[nextY][nextX]) continue;

            // 색맹일 경우 color가 R 또는 G라면 둘다 방문 가능
            if(mang && (color == 'R' || color == 'G')) {
                if(board[nextY][nextX] == 'R' || board[nextY][nextX] == 'G') {
                    q.push(make_pair(nextY, nextX));
                    visited[nextY][nextX] = true;
                }
                continue;
            }

            // 다음 컬러와 같아야함
            if(board[nextY][nextX] == color) {
                q.push(make_pair(nextY, nextX));
                visited[nextY][nextX] = true;
            }
        }
    }

    return;
}

int bfsAll(bool mang) {
    int ret = 0;
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x) {
            if(!visited[y][x]) {
                bfs(y, x, mang);
                ret++;
            }
        }
    return ret;
}

int main(void) {
    cin >> N;
    board.resize(N, vector<char>(N));
    visited.resize(N, vector<bool>(N, false));

    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x)
            cin >> board[y][x];

    cout << bfsAll(false) << ' ';

    visited.clear();
    visited.resize(N, vector<bool>(N, false));

    cout << bfsAll(true) << endl;

    return 0;
}
