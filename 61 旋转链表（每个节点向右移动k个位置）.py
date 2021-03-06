# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k: return head
        tmp, count= head, 0
        while tmp:
            tmp = tmp.next
            count += 1
        k = k % count
        if k == 0:
            return head
        fast = slow = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead