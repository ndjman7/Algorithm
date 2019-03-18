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
        // 결과로 반환할 ListNode.
        ListNode* root;
        // 첫번째 Node를 만듬.
        ListNode* node = new ListNode(l1->val + l2->val);
        if(node->val / 10) {
            ListNode* new_node = new ListNode(node->val / 10);
            node->val %= 10;
            node->next = new_node;
        }
        l1 = l1->next;
        l2 = l2->next;
        root = node;
        
        // 둘 중 하나라도 NULL이 아닐때 까지 계속 반복.
        while(l1 != NULL || l2 != NULL) {
            // node의 next가 NULL이 아니라면, 그 전에 carry된 값이 있다는 것.
            int l1_val = l1 ? l1->val : 0;
            int l2_val = l2 ? l2->val : 0;
            if(node->next) {
                node = node->next;
                node->val = node->val + l1_val + l2_val;
            }
            else {
                ListNode* new_node = new ListNode(l1_val + l2_val);
                node->next = new_node;
                node = node->next;
            }

            if(node->val / 10) {
                ListNode* new_node = new ListNode(node->val / 10);
                node->val %= 10;
                node->next = new_node;
            }

            if(l1 != NULL)
                l1 = l1->next;
            if(l2 != NULL)
                l2 = l2->next;

        }
        return root;
    }
};
