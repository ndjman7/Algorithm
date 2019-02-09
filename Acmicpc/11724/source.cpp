#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > adj;
vector<bool> visited;
int V, E;

void dfs(int here) {
    visited[here] = true;
    for(int i = 0; i < adj[here].size(); ++i) {
        int there = adj[here][i];
        if(!visited[there])
            dfs(there);
    }
    return;
}

int dfsAll() {
    int cnt = 0;
    for(int i = 1; i <= V; ++i)
        if(!visited[i]) {
            dfs(i);
            cnt++;
        }
    return cnt;
}

int main(void) {
    cin >> V >> E;
    int v1, v2;
    adj.resize(V+1);
    visited.resize(V+1, false);
    for(int i = 0; i < E; ++i) {
        cin >> v1 >> v2;
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }

    cout << dfsAll() << endl;;

    return 0;
}
