#include <iostream>

using namespace std;

#define MAXVALUE 1001

int A[MAXVALUE];
int cache[MAXVALUE];
int N;

int dp(int index) {
    if(index == N) return A[N];
    int& ret = cache[index];
    if(ret != -1) return ret;
    ret = A[index];
    int maxValue = 0;
    for(int i = index+1; i <= N; ++i)
        if(A[index] < A[i])
            maxValue = max(maxValue, dp(i));
    ret += maxValue;
    return ret;
}
int main(void) {
    cin >> N;
    A[0] = 0;
    cache[0] = -1;
    for(int i = 1; i <= N; ++i) {
        cin >> A[i];
        cache[i] = -1;
    }
    dp(0);
    cout << cache[0] << endl;
    return 0;
}
