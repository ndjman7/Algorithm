#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int Y, X;
vector<vector<char> > board;
vector<vector<bool> > visited;
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
queue<pair<int, int> > water;
queue<pair<int, int> > hedgehog;
int answer;

bool bfs() {
    while(!hedgehog.empty()) {
        // 물부터 이동
        int h_size = hedgehog.size();
        if(h_size == 0) break;
        answer++;
        int w_size = water.size();
        while(w_size) {
            pair<int, int> w = water.front();
            water.pop();
            for(int i = 0; i < 4; ++i) {
                int nextY = w.first + dy[i];
                int nextX = w.second + dx[i];

                if(nextY < 0 || nextX < 0 || nextY >= Y || nextX >= X)
                    continue;
                if(visited[nextY][nextX])
                    continue;
                if(board[nextY][nextX] == 'D' || board[nextY][nextX] == 'S' || board[nextY][nextX] == 'X')
                    continue;
                visited[nextY][nextX] = true;
                water.push(make_pair(nextY, nextX));
            }
            w_size--;
        }

        while(h_size) {
            pair<int, int> h = hedgehog.front();
            hedgehog.pop();

            for(int i = 0; i < 4; ++i) {
                int nextY = h.first + dy[i];
                int nextX = h.second + dx[i];

                if(nextY < 0 || nextX < 0 || nextY >= Y || nextX >= X)
                    continue;
                if(visited[nextY][nextX])
                    continue;
                if(board[nextY][nextX] == '.') {
                    hedgehog.push(make_pair(nextY, nextX));
                    visited[nextY][nextX] = true;
                }
                if(board[nextY][nextX] == 'D')
                    return true;
            }
            h_size--;
        }
    }
    return false;
}

int main(void) {
    cin >> Y >> X;
    board.resize(Y, vector<char>(X));
    visited.resize(Y, vector<bool>(X, false));

    for(int y = 0; y < Y; ++y)
        for(int x = 0; x < X; ++x) {
            cin >> board[y][x];
            if(board[y][x] == 'S') {
                hedgehog.push(make_pair(y, x));
                visited[y][x] = true;
            }
            else if(board[y][x] == '*') {
                water.push(make_pair(y, x));
                visited[y][x] = true;
            }
        }

    if(bfs())
        cout << answer;
    else
        cout << "KAKTUS";

    return 0;
}
