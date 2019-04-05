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
    ListNode* returnNext(ListNode* node, int val) {
        ListNode* curr = node;
        while(true) {
            if(curr->val != val)
                break;
            node->next = curr->next;
            curr = curr->next;
        }
        return node;
    }
    
    ListNode* removeElements(ListNode* head, int val) {
        if(head==NULL)
            return head;
        ListNode* curr = head;
        if(curr->val == val)
            head = head->next;
        
        if(curr->next == NULL)
            return head;
        
        
        return head;
    }
};
