#include <iostream>

using namespace std;

#define MAXNUMBER 1001

int A[MAXNUMBER];
int cache[MAXNUMBER];
int N;

int dp(int index) {
    if(index == N) return 1;

    int& ret = cache[index];
    if(ret != -1) return ret;

    ret = 1;

    int maxValue = 0;
    for(int nextIndex = index+1; nextIndex <= N; ++nextIndex) {
        if(A[index] > A[nextIndex])
            maxValue = max(maxValue, dp(nextIndex));
    }

    ret += maxValue;
    return ret;
}

int main(void) {
    cin >> N;
    A[0] = MAXNUMBER;
    cache[0] = -1;
    for(int i = 1; i <= N; ++i) {
        cin >> A[i];
        cache[i] = -1;
    }

    dp(0);
    cout << cache[0] - 1<< endl;

    return 0;
}
