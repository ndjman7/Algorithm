#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > board;
vector<vector<bool> > visited;
vector<pair<int, int> > virus;
int Y, X, safeZoneCount, maxSafe, minVirus = 100;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int dfs(int y, int x) {
    visited[y][x] = true;
    int cnt = 1;
    for(int i = 0; i < 4; ++i) {
        int nextY = y + dy[i];
        int nextX = x + dx[i];

        if(nextY < 0 || nextX < 0 || nextY >= Y || nextX >= X)
            continue;

        if(visited[nextY][nextX])
            continue;

        if(board[nextY][nextX] != 0)
            continue;

        cnt += dfs(nextY, nextX);
    }
    return cnt;
}

void speadVirus() {
    visited.clear();
    visited.resize(Y, vector<bool>(X, false));

    int newVirus = 0;
    for(int i = 0; i < virus.size(); ++i) {
        newVirus += dfs(virus[i].first, virus[i].second) -1;
        if(minVirus < newVirus)
            return;
    }

    // 새롭게 퍼진 바이러스 수
    maxSafe = max(maxSafe, safeZoneCount - newVirus);
    minVirus = min(minVirus, newVirus);
    return;
}

void setWall(int depth, int prevY, int prevX) {
    if(depth==3) {
        speadVirus();
        return;
    }

    for(int y = 0; y < Y; ++y) {
        for(int x = 0; x < X; ++x) {
            if(board[y][x] != 0)
                continue;
            if((prevY == y && prevX <= x) || prevY < y) {
                board[y][x] = 1;
                setWall(depth + 1, y, x);
                board[y][x] = 0;
            }
        }
    }
    return;
}

int main(void) {
    cin >> Y >> X;
    board.resize(Y, vector<int>(X));

    for(int y = 0; y < Y; ++ y)
        for(int x = 0; x < X; ++x) {
            cin >> board[y][x];
            if(board[y][x] == 2)
                virus.push_back(make_pair(y, x));
            if(board[y][x] == 0)
                safeZoneCount++;
        }
    safeZoneCount -= 3;

    setWall(0, 0, 0);
    cout << maxSafe << endl;
    return 0;
}
