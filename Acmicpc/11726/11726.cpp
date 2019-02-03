#include <iostream>
using namespace std;

const int MOD = 10007;
int cache[1001];

int tiling(int n) {
    if(n <= 1)
        return 1;

    int& ret = cache[n];
    if(ret != -1) return ret;

    return ret = (tiling(n-1) + tiling(n-2)) % MOD;
}

int main(void) {
    int N;
    cin >> N;
    for(int i = 0; i <= N; ++i)
        cache[i] = -1;

    cout << tiling(N) << endl;

    return 0;
}
