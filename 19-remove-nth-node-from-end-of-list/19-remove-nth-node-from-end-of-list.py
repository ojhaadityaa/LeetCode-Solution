# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start,end=head,head
        for _ in range (0,n):
            end=end.next
            if end==None:
                return start.next
            n-=1
        while end.next!=None:
            end=end.next
            start=start.next
        start.next=start.next.next
        return head
            
        