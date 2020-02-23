# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        linked_list = head
        cnt = 1
        while True:
            if linked_list.next is None:
                break
            cnt += 1
            linked_list = linked_list.next

        middle = int(cnt/2) + 1
        find = 1
        while True:
            if find == middle:
                break
            find += 1
            head = head.next

        return head
