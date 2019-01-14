#include <iostream>
using namespace std;

bool check[10][10];
bool friends[10];
int C, n, m;

bool finish() {
    for(int i = 0; i < n; ++i)
        if(!friends[i])
            return false;
    return true;
}

int count(int start) {
    int ret = 0;
    if(finish()) return 1;

    for(int i = start; i < n; ++i) {
        if(!friends[i]) friends[i] = true;
        else continue;
        for(int j = i+1; j < n; ++j) {
            if(!friends[j] && check[i][j]) {
                friends[j] = true;
                ret += count(i+1);
                friends[j] = false;
            }
        }
        friends[i] = false;
    }
    return ret;
}

int main(void) {
    int a, b;
    cin >> C;
    for(int t = 0; t < C; ++t) {
        cin >> n >> m;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j)
                check[i][j] = false;
            friends[i] = false;
        }

        for(int i = 0; i < m; ++i) {
            cin >> a >> b;
            if(a > b)
                check[b][a] = true;
            else
                check[a][b] = true;
        }

        cout << count(0) << endl;
    }
    return 0;
}
