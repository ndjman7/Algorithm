#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > board;
vector<vector<int> > adj;
int N;

void dfs(int start, int y) {

    for(int i = 0; i < N; ++i)
        if(board[y][i] == 1 && adj[start][i] == 0) {
            adj[start][i] = 1;
            dfs(start, i);
        }
}

void dfsAll() {
    for(int y = 0; y < N; ++y)
        dfs(y, y);
}

int main(void) {
    cin >> N;
    board.resize(N, vector<int>(N));
    adj.resize(N, vector<int>(N, 0));
    for(int y = 0; y < N; ++y)
        for(int x = 0; x < N; ++x)
            cin >> board[y][x];
    dfsAll();
    for(int y = 0; y < N; ++y) {
        for(int x = 0; x < N; ++x)
            cout << adj[y][x] << ' ';
        cout << endl;
    }

    return 0;
}
