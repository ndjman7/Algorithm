#include <iostream>
#include <vector>

using namespace std;

vector<vector<char> > board;
vector<bool> alpha;

int Y, X;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int dfs(int y, int x) {
    alpha[board[y][x] - 'A'] = true;
    int cnt = 0;
    for(int i = 0; i < 4; ++i) {
        int nextY = y + dy[i];
        int nextX = x + dx[i];

        if(nextY < 0 || nextX < 0 || nextY >= Y || nextX >= X)
            continue;

        if(alpha[board[nextY][nextX] - 'A'])
            continue;

        cnt = max(cnt, dfs(nextY, nextX));
    }
    alpha[board[y][x] - 'A'] = false;
    return ++cnt;
}

int main(void) {
    cin >> Y >> X;
    board.resize(Y, vector<char>(X));
    for(int y = 0; y < Y; ++y)
        for(int x = 0; x < X; ++x) {
            cin >> board[y][x];
        }
    alpha.resize(26, false);
    cout << dfs(0, 0) << endl;
    return 0;
}
