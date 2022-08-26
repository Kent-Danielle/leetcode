# https://binarysearch.com/room/buffer-overflow-Sdl02i9EOI
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        slow, fast = node, node.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return slow.val