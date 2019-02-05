#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

vector<vector<int> > adj;
vector<int> visited;
int K, V, E;
bool check;
vector<string> answer;

void bfs(int start, int team) {
    queue<int> q;
    // 처음은 1팀
    visited[start] = team;
    q.push(start);
    while(!q.empty()) {
        int here = q.front();
        q.pop();
        for(int v = 0; v < adj[here].size(); ++v) {
            int there = adj[here][v];
            // 인접한 노드는 반대의 팀으로 구성
            if(visited[there] == 0) {
                visited[there] = visited[here] * -1;
                q.push(there);
            }
            // 방문을 했는데 인접한 노드랑 같다면 no
            else if(visited[there] == visited[here]) {
                check = true;
                return;
            }
        }
    }
}

int main(void) {
    cin >> K;
    int v1, v2;
    for(int i = 0; i < K; ++i) {
        adj.clear();
        cin >> V >> E;
        adj.resize(V+1);
        visited.clear();
        visited.resize(V+1, 0);
        for(int e = 0; e < E; ++e) {
           cin >> v1 >> v2;
           adj[v1].push_back(v2);
           adj[v2].push_back(v1);
        }
        for(int i = 1; i <= V; ++i) {
            if(check)
                break;
            if(visited[i] == 0)
                bfs(i, 1);
        }
        answer.push_back(check? "NO" : "YES");
        check = false;
    }

    for(int i = 0; i < answer.size(); ++i)
        cout << answer[i] << endl;
    return 0;
}
