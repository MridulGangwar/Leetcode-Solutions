"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def traverse(root,level):
            if len(result)==level:
                result.append([])
            result[level].append(root.val)
            for c in root.children:
                traverse(c,level+1)
        
        result = []
        
        if root is not None:
            traverse(root,0)
            
        return result