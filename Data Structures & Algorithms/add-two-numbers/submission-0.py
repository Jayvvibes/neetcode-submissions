# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        temp = l1
        while temp:
            s1 += str(temp.val)
            temp = temp.next
        s2 = ""
        temp = l2
        while temp:
            s2 += str(temp.val)
            temp = temp.next
        s1 = s1[::-1]
        s2 = s2[::-1]
        r = int(s1) + int(s2)
        r = str(r)
        r = r[::-1]
        dummy = ListNode(-1)
        cur = dummy
        for c in r:
            cur.next = ListNode(c)
            cur = cur.next
        return dummy.next