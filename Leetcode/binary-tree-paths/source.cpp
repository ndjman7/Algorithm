/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<string> ans;
    void returnPath(TreeNode* node, string path) {
        path += to_string(node->val);
        if(node->left != NULL) {
            string newPath = path + "->";
            returnPath(node->left, newPath);
        }
        if(node->right != NULL) {
            string newPath = path + "->";
            returnPath(node->right, newPath);
        }
        if(node->left == NULL && node->right == NULL) {
            ans.push_back(path);
        }
        return;
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        if(root != NULL)
            returnPath(root, "");
        return ans;
    }
};
