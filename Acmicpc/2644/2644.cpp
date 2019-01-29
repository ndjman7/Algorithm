#include <iostream>
#include <queue>
#include <vector>
using namespace std;

queue<int> q;
vector<vector<int> > adj;
vector<int> dist;
int V, E, start, en;

void bfs(int start) {
    q.push(start);
    dist[start] = 0;
    while(!q.empty()) {
        int here = q.front();
        q.pop();
        for(int v = 0; v < adj[here].size(); ++v) {
            int there = adj[here][v];
            if(dist[there] == -1) {
                q.push(there);
                dist[there] = dist[here] + 1;
            }
        }
    }
    return;
}

int main(void) {
    cin >> V >> start >> en >> E;
    int v1, v2;
    adj.resize(V+1);
    dist.resize(V+1, -1);

    for(int i = 0; i < E; ++i) {
        cin >> v1 >> v2;
        adj[v1].push_back(v2);
        adj[v2].push_back(v1);
    }
    bfs(start);
    cout << dist[en] << endl;
    return 0;
}
