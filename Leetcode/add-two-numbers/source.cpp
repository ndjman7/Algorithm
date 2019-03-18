/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* root;
        ListNode node(l1->val + l2->val);
        l1 = l1->next;
        l2 = l2->next;
        root = &node;
        while(l1 != NULL || l2 != NULL) {
            if(node.next) {
                node = *(node.next);
                node.val = node.val + l1->val + l2->val;
            }
            else {
                ListNode new_node(l1->val + l2->val);
                node.next = &new_node;
                node = *(node.next);
            }
            
            if(node.val / 10) {
                node.val %= 10;
                ListNode new_node(node.val / 10);
                node.next = &new_node;
            }
            
            l1 = l1->next;
            l2 = l2->next;

        }
        return root;  
    }
};
