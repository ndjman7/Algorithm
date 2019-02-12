#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > board;
vector<vector<bool> > visited;
int N, H;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

void dfs(int y, int x) {
    visited[y][x] = true;

    for(int i = 0; i < 4; ++i) {
        int nextY = y + dy[i];
        int nextX = x + dx[i];

        if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= N)
            continue;

        if(visited[nextY][nextX])
            continue;

        if(board[nextY][nextX] <= H)
            continue;

        dfs(nextY, nextX);
    }
}

int dfsAll() {
    int cnt = 0;
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x)
            if(!visited[y][x] && board[y][x] > H) {
                dfs(y, x);
                cnt++;
            }
    return cnt;
}

int main(void) {
    int ans = 1, minValue = 100, maxValue = 0;
    cin >> N;
    board.resize(N, vector<int>(N));
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x) {
            cin >> board[y][x];
            maxValue = max(maxValue, board[y][x]);
            minValue = min(minValue, board[y][x]);
        }

    for(int i = minValue; i < maxValue; ++i) {
        visited.clear();
        visited.resize(N, vector<bool>(N, false));
        H = i;
        ans = max(ans, dfsAll());
    }
    cout << ans << endl;
    return 0;
}
