#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > board;
vector<vector<bool> > visited;
vector<int> ans;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
int Y, X, K;

int dfs(int y, int x) {
    visited[y][x] = true;
    int cnt = 1;
    for (int i = 0; i < 4; ++i) {
        int nextY = y + dy[i];
        int nextX = x + dx[i];
        if(nextY < 0 || nextX < 0 || nextY >= Y || nextX >= X)
            continue;
        if(visited[nextY][nextX])
            continue;
        if(board[nextY][nextX] == 1)
            continue;
        cnt += dfs(nextY, nextX);
    }
    return cnt;
}

int dfsAll() {
    int cnt = 0;
    for(int y = 0; y < Y; ++y)
        for(int x = 0; x < X; ++x)
            if(!visited[y][x] && board[y][x] == 0) {
                ans.push_back(dfs(y, x));
                cnt++;
            }
    return cnt;
}

int main(void) {
    cin >> Y >> X >> K;
    board.resize(Y, vector<int>(X, 0));
    visited.resize(Y, vector<bool>(X, false));
    int x1, y1, x2, y2;
    for(int i = 0; i < K; ++i) {
        cin >> x1 >> y1 >> x2 >> y2;
        for(int y = y1; y < y2; ++y)
            for(int x = x1; x < x2; ++x)
                board[y][x] = 1;
    }
    cout << dfsAll() << endl;

    sort(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); ++i)
        cout << ans[i] << ' ';
    cout << endl;

    return 0;
}
