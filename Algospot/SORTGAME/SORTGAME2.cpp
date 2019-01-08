#include <map>
#include <queue>
#include <vector>
#include <iostream>
using namespace std;

map<vector<int>, int> toSort;

void precalc(int n) {
    vector<int> perm(n);
    for(int i = 0; i < n; ++i) perm[i] = i;
    queue<vector<int> > q;
    q.push(perm);
    toSort[perm] = 0;
    while(!q.empty()) {
        vector<int> here = q.front();
        q.pop();
        int cost = toSort[here];
        for(int i = 0; i < n; ++i) {
            for(int j = i+2; j <= n; ++j) {
                reverse(here.begin() + i, here.begin() +j);
                if(toSort.count(here) == 0) {
                    toSort[here] = cost + 1;
                    q.push(here);
                }
                reverse(here.begin() + i, here.begin() +j);
            }
        }
    }
}
int solve(const vector<int>& perm) {
    int n = perm.size();
    vector<int> fixed(n);
    for(int i = 0; i < n; ++i) {
        int smaller = 0;
        for(int j = 0; j < n; ++j)
            if(perm[j] < perm[i])
                ++smaller;
        fixed[i] = smaller;
    }
    return toSort[fixed];
}

int main(void) {
    int n, C, value;
    vector<int> arr;
    cin >> C;
    for(int t = 0; t < C; ++t) {
        arr.clear();
        cin >> n;
        precalc(n);
        for(int i = 0; i < n; ++i) {
            cin >> value;
            arr.push_back(value);
        }
        cout << solve(arr) << endl;
    }
    return 0;
}
