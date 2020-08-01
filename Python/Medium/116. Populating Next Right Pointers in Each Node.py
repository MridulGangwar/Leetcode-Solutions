from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        stack = deque()
        stack.append(root)
        
        while stack:
            length = len(stack)
            prev = None
            
            for _ in range(length):
                curr = stack.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                    
        return root