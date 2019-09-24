#include <iostream>
#include <queue>

using namespace std;

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    priority_queue<int> pq;

    int size, value;
    cin >> size;
    for (int i = 0; i < size; i++) {
        cin >> value;
        if (value == 0) {
            if (pq.empty())
                cout << 0 << "\n";
            else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
            pq.push(value);
    }

    return 0;
}
