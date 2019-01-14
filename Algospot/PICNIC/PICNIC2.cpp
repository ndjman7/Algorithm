#include <iostream>
using namespace std;

bool areFriends[10][10];
int C, n, m;

int countPairings(bool taken[10]) {
    int firstFree = -1;
    for(int i = 0; i < n; ++i) {
        if(!taken[i]) {
            firstFree = i;
            break;
        }
    }

    if(firstFree == -1) return 1;
    int ret = 0;

    for(int pairWith = firstFree+1; pairWith < n; ++pairWith) {
        if(!taken[pairWith] && areFriends[firstFree][pairWith]) {
            taken[firstFree] = taken[pairWith] = true;
            ret += countPairings(taken);
            taken[firstFree] = taken[pairWith] = false;
        }
    }
    return ret;
}

int main(void) {
    int a, b;
    cin >> C;
    bool taken[10];
    for(int t = 0; t < C; ++t) {
        cin >> n >> m;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j)
                areFriends[i][j] = false;
            taken[i] = false;
        }

        for(int i = 0; i < m; ++i) {
            cin >> a >> b;
            if(a > b)
                areFriends[b][a] = true;
            else
                areFriends[a][b] = true;
        }

        cout << countPairings(taken) << endl;
    }
    return 0;
}
