#include <iostream>
#include <queue>
using namespace std;

#define MAX_VALUE 100000
bool visited[MAX_VALUE+1];

int bfs(int n, int k) {
    int ret = 0;
    queue<int> q;
    q.push(n);
    while(1) {
        int size = q.size();
        for(int v = 0; v < size; ++v) {
            n = q.front();
            q.pop();
            if(n == k)
                return ret;
            if(n > 0 && !visited[n-1]) {
                q.push(n-1);
                visited[n-1] = true;
            }
            if(n < MAX_VALUE && !visited[n+1]) {
                q.push(n+1);
                visited[n+1] = true;
            }
            if(n*2 <= MAX_VALUE && !visited[n*2]) {
                q.push(n*2);
                visited[n*2] = true;
            }
        }
        ret++;
    }
}

int main(void) {
    int N, K;
    cin >> N >> K;
    cout << bfs(N, K) << endl;
    return 0;
}
