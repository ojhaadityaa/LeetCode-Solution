# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l,r=head,head
        while n!=0:
            r=r.next
            if r==None:
                return l.next
            n-=1
        while r.next:
            r=r.next
            l=l.next
        l.next=l.next.next
        return head