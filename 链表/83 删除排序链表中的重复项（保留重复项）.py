# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        cur, next = head, head.next
        while cur and next:
            if next.val != cur.val: cur = cur.next
            else: cur.next = next.next
            next = next.next

        return head