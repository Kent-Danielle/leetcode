from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        doubleQueue = deque([])
        pointer = head.next
        while pointer != None:
            doubleQueue.append(pointer)
            pointer = pointer.next
            
        switch = False
        while head != None:
            if len(doubleQueue) == 0:
                head.next = None
                break
            
            if not switch:
                head.next = doubleQueue.pop()
            else:
                head.next = doubleQueue.popleft()
            switch = not switch
            head = head.next