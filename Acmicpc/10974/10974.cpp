#include <iostream>
using namespace std;

int N;
int arr[8];
bool used[8];

void all(int idx) {
    if (idx == N) {
        for(int i = 0; i < N; ++i)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }

    for(int i = 0; i < N; ++i) {
        // 아직 사용하지 않았다면 배열에 넣어줌
        if(!used[i]) {
            // 사용했다고 체크
            used[i] = true;
            // 정답 배열에 값을 넣어줌
            arr[idx] = i+1;
            // 다음 인덱스로 함수 호출
            all(idx+1);
            // 다시 사용하지 않는다고 말해줌
            used[i] = false;
        }
    }
    return;
}

int main(void) {
    cin >> N;
    for(int i = 0; i < N; ++i)
        used[i] = false;
    all(0);
    return 0;
}
