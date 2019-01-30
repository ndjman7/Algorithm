#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<bool> > board;
int l, sy ,sx ,ey, ex;
int dy[8] = {-1, 1, -1, 1, 2, -2, 2, -2};
int dx[8] = {2, 2, -2, -2, -1, -1, 1, 1};
vector<int> ans;

int bfs() {
    queue<pair<int, int> > q;
    pair<int, int> p;
    int answer = 0, size = 0;;
    board[sy][sx] = true;
    p = make_pair(sy, sx);
    q.push(p);
    while(true) {
        if(q.empty()) break;
        size = q.size();
        while(size) {
            p = q.front();
            if(p.first == ey && p.second == ex)
                return answer;
            q.pop();
            for(int d = 0; d < 8; ++d) {
                int nextY = p.first + dy[d];
                int nextX = p.second + dx[d];
                if(nextY < 0 || nextX < 0 || nextY >= l || nextX >= l)
                    continue;
                if(!board[nextY][nextX]) {
                    board[nextY][nextX] = true;
                    q.push(make_pair(nextY, nextX));
                }
            }
            size--;
        }
        answer++;
    }
    return answer;
}

int main(void) {
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t) {
        cin >> l;
        board.clear();
        board.resize(l, vector<bool>(l, false));
        cin >> sy >> sx;
        cin >> ey >> ex;
        ans.push_back(bfs());
    }
    for(int i = 0; i < ans.size(); ++i)
        cout << ans[i] << endl;
    return 0;
}
