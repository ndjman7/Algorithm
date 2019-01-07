#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > adj;

void bfs2(int start, vector<int>& distance, vector<int>& parent) {
    distance = vector<int>(adj.size(), -1);
    parent = vector<int>(adj.size(), -1);
    queue<int> q;
    distance[start] = 0;
    parent[start] = start;
    q.push(start);
    while(!q.empty()) {
        int here = q.front();
        q.pop();
        for(int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i];
            if(distance[there] == -1) {
                q.push(there);
                distance[there] = distance[here] + 1;
                parent[there] = here;
            }
        }
    }
}

vector<int> shortestPath(int v, const vector<int>& parent) {
    vector<int> path(1, v);
    while(parent[v] != v) {
        v = parent[v];
        path.push_back(v);
    }
    reverse(path.begin(), path.end());
    return path;
}

int main(void) {
    return 0;
}
