#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > adj;
vector<bool> visited;
queue<int> q;

void dfs(int here) {
    visited[here] = true;
    cout << here << " ";
    for(int v = 0; v < adj[here].size(); ++v) {
        int there = adj[here][v];
       if(!visited[there])
            dfs(there);
    }
    return;
}

void bfs(int start) {
    visited[start] = true;
    cout << start << ' ';
    q.push(start);
    while(!q.empty()) {
        int here = q.front();
        q.pop();
        for(int v = 0; v < adj[here].size(); ++v) {
            int there = adj[here][v];
            if(!visited[there]) {
                q.push(there);
                visited[there] = true;
                cout << there << ' ';
            }
        }
    }
    cout << '\n';
    return;
}

int main(void) {
    int N, M, V;
    int v1, v2;
    cin >> N >> M >> V;
    visited.resize(N+1, false);
    adj.resize(N+1);
    for(int i = 0; i < M; ++i) {
        cin >> v1 >> v2;
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }
    for(int i = 1; i <= N; ++i)
        sort(adj[i].begin(), adj[i].end());

    dfs(V);
    cout << '\n';
    visited.clear();
    visited.resize(N+1, false);
    bfs(V);
    return 0;
}

