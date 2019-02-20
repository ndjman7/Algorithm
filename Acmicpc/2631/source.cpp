#include <iostream>

using namespace std;

int N;
int A[201];
int cache[201];

int dp(int index) {
    if(index==N) return 1;
    int& ret = cache[index];
    if(ret != -1) return ret;

    ret = 1;
    int maxValue = 0;
    for(int i = index+1; i <= N; ++i)
        if(A[index] < A[i])
            maxValue = max(maxValue, dp(i));
    ret += maxValue;

    return ret;
}

int main(void) {
    cin >> N;
    A[0] = cache[0] = -1;
    for(int i = 1; i <= N; ++i) {
        cin >> A[i];
        cache[i] = -1;
    }

    dp(0);

    cout << N - cache[0] + 1 << endl;

    return 0;
}
