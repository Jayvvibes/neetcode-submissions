# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        if l == n:
            return head.next

        k = l - n - 1
        temp = head
        for _ in range(k):
            temp = temp.next

        temp.next = temp.next.next

        return head