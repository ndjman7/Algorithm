#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > board;
vector<vector<bool> > visited;
int Y, X;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

void dfs(int y, int x) {
    visited[y][x] = true;
    for(int d = 0; d < 4; ++d) {
        int nextY = y + dy[d];
        int nextX = x + dx[d];
        if(nextY < 0 || nextX < 0 || nextY >= Y || nextX >= X)
            continue;
        if(!visited[nextY][nextX] && board[y][x] == 1)
            dfs(nextY, nextX);
    }
}

int dfsAll() {
    int cnt = 0;
    for(int y = 0; y < Y; ++y)
        for(int x= 0; x < X; ++x) {
            if(!visited[y][x] && board[y][x] == 1) {
                dfs(y, x);
                cnt++;
            }
        }
    return cnt;
}

int main(void) {
    int testCase, K, y, x;
    cin >> testCase;
    for(int t = 0; t < testCase; ++t) {
        cin >> Y >> X >> K;
        board.clear();
        board.resize(Y, vector<int>(X, 0));
        visited.clear();
        visited.resize(Y, vector<bool>(X, false));
        for(int k = 0; k < K; ++k) {
            cin >> y >> x;
            board[y][x] = 1;
        }
        cout << dfsAll() << endl;
    }
    return 0;
}
