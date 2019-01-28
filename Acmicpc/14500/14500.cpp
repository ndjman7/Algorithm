#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<vector<int> > board;
vector<vector<bool> > visited;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int tetri(int depth, int y, int x, int ret) {
    ret += board[y][x];

    // 4칸을 이동했다면
    if(depth == 3)
        return ret;
    visited[y][x] = true;

    // 최대값
    int ans = ret;

    for(int d = 0; d < 4; ++d) {
        // 상화좌우
        int nextY = y + dy[d];
        int nextX = x + dx[d];
        // 범위를 벗어났다면
        if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= M)
            continue;
        // 이미 방문했다면
        if(visited[nextY][nextX])
            continue;
        ans = max(ans, tetri(depth+1, nextY, nextX, ret));
    }
    // 종료할 때는 현재 위치를 방문하지 않은 것으로 수정
    visited[y][x] = false;
    return ans;
}

int other(int y, int x) {
    int cnt = 0, ret = board[y][x], ans = 0;
    for(int d = 0; d < 4; ++d) {
        int nextY = y + dy[d];
        int nextX = x + dx[d];
        if(nextY < 0 || nextX < 0 || nextY >= N || nextX >= M)
            continue;
        ret += board[nextY][nextX];
        cnt++;
    }
    if(cnt!=4)
        return ret;
    for(int d = 0; d < 4; ++d) {
        int nextY = y + dy[d];
        int nextX = x + dx[d];
        ret -= board[nextY][nextX];
        ans = max(ans, ret);
        ret += board[nextY][nextX];
    }
    return ans;
}

int problem() {
    int ans = 0;
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < M; ++x) {
            ans = max(ans, other(y, x));
            ans = max(ans, tetri(0, y, x, 0));
        }
    return ans;
}

int main(void) {
    cin >> N >> M;

    board.resize(N, vector<int>(M));
    visited.resize(N, vector<bool>(M, false));

    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j)
            cin >> board[i][j];

    cout << problem() << endl;
    return 0;
}
