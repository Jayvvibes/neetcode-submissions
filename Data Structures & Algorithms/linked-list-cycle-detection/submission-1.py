# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        arr = []
        while temp:
            if temp in arr:
                return True
            arr.append(temp)
            temp = temp.next
        return False