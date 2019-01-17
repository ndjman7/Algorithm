#include <vector>
#include <iostream>
using namespace std;

vector<vector<int> > adj;

void makeGraph(const vector<string>& words) {
    adj = vector<vector<int> >(26, vector<int>(26, 0));
    for(int j = 1; j < words.size(); ++j) {
        int i = j - 1, len = min(words[i].size(), words[j].size());
        for(int k = 0; k < len; ++k)
            if(words[i][k] != words[j][k]) {
                int a = words[i][k] - 'a';
                int b = words[j][k] - 'a';
                adj[a][b] = 1;
                break;
            }
    }
}

vector<int> seen, order;
void dfs(int here) {
    seen[here] = 1;
    for(int there = 0; there < adj.size(); ++there)
        if(adj[here][there] && !seen[there])
            dfs(there);
    order.push_back(here);
}

vector<int> topologicalSort() {
    int n = adj.size();
    seen = vector<int>(n, 0);
    order.clear();
    for(int i = 0; i < n; ++i) if(!seen[i]) dfs(i);
    reverse(order.begin(), order.end());
    for(int i = 0; i < n; ++i)
        for(int j = i+1; j < n; ++j)
            if(adj[order[j]][order[i]])
                return vector<int>();
    return order;
}

int main(void) {
    int C, n;
    cin >> C;
    vector<string> words;
    string word;
    vector<int> result;
    for(int t = 0; t < C; ++t) {
        cin >> n;
        words.clear();
        for(int i = 0; i < n; ++i) {
            cin >> word;
            words.push_back(word);
        }
        makeGraph(words);
        result = topologicalSort();
        if(result.size() == 0)
            cout << "INVALID HYPOTHESIS";
        for(int i = 0; i < result.size(); ++i)
            cout << char(result[i] + 'a');
        cout << endl;
    }
    return 0;
}
