#include <iostream>
#include <vector>

using namespace std;

vector<int> slice(const vector<int>& v, int a, int b) {
    return vector<int>(v.begin() + a, v.begin() + b);
}

void printPostOrder(const vector<int>& preorder, const vector<int>& inorder) {
    const int N = preorder.size();
    if(preorder.empty()) return;
    const int root = preorder[0];
    const int L = find(inorder.begin(), inorder.end(), root) - inorder.begin();
    const int R = N - 1 - L;
    printPostOrder(slice(preorder, 1, L+1), slice(inorder, 0, L));
    printPostOrder(slice(preorder, L+1, N), slice(inorder, L+1, N));
    cout << root << ' ';
}

int main(void) {
    vector<int> preorder, inorder;
    int testCase, size, node;
    cin >> testCase;
    for(int i = 0; i < testCase; ++i) {
        preorder.clear();
        inorder.clear();
        cin >> size;
        for(int n = 0; n < size; ++n) {
            cin >> node;
            preorder.push_back(node);
        }
        for(int n = 0; n < size; ++n) {
            cin >> node;
            inorder.push_back(node);
        }
        printPostOrder(preorder, inorder);
        cout << endl;
   }
    return 0;
}
