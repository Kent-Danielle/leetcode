# https://binarysearch.com/room/buffer-overflow-Sdl02i9EOI
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        left = LLNode(0,next=node)
        right = LLNode(0)
        
        temp = left
        for _ in range(k + 1):
            temp = temp.next
            right = temp

        
        while right:
            left = left.next
            right = right.next
        
        return left.val
        

