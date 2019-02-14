#include <iostream>

using namespace std;

#define LENGTH 1001

int A[LENGTH];
int cache[LENGTH];
int N;

int dp(int idx) {
    // N이면 1을 반환
    if(idx == N) return 1;

    int& ret = cache[idx];
    if(ret != -1) return ret;

    // 자기자신 카운트
    ret = 1;
    int maxValue = 0;
    // 재귀호출 중에서 가장 큰 값을 찾음
    for(int i = idx+1; i <= N; ++i)
        if(A[idx] < A[i])
            maxValue = max(maxValue, dp(i));

    // 가장 큰 값을 더함
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
    cout << cache[0] - 1 << endl;
    return 0;
}
