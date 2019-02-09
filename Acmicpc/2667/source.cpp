#include <iostream>
#include <vector>

using namespace std;

vector<vector<char> > board;
vector<vector<bool> > visited;
vector<int> ans;
int N;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int dfs(int y, int x) {
    int cnt = 1;
    visited[y][x] = true;
    for(int i = 0; i < 4; ++i) {
        int nextY = y + dy[i];
        int nextX = x + dx[i];

        if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= N)
            continue;

        if(visited[nextY][nextX])
            continue;

        if(board[nextY][nextX] == '0')
            continue;

        cnt += dfs(nextY, nextX);
    }
    return cnt;
}

int dfsAll() {
    int cnt = 0;
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x)
            if(!visited[y][x] && board[y][x] == '1') {
                ans.push_back(dfs(y, x));
                cnt++;
            }
    return cnt;
}

int main(void) {
    cin >> N;
    board.resize(N, vector<char>(N));
    visited.resize(N, vector<bool>(N, false));
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x)
            cin >> board[y][x];

    cout << dfsAll() << endl;
    sort(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); ++i)
        cout << ans[i] << endl;

    return 0;
}
