# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return head
        
        tmp = head
        right = ListNode()
        for _ in range(n):
            tmp = tmp.next
            right = tmp
        left = ListNode(next=head)
        
        while right:
            left = left.next
            right = right.next
            
        if left.next == head and not right:
            head = left.next.next
        else:
            left.next = left.next.next
        return head
        