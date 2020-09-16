# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            successor = node
        else:
            node = root
            while node:
                if node.val == p.val:
                    break
                elif p.val > node.val:
                    node = node.right
                else:
                    successor = node
                    node = node.left
        
        return successor
        
		
		
		
		
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        curr, candidate = root, None   
        while curr:
            if curr.val>p.val:
                candidate = curr
                curr = curr.left
            else:
                curr = curr.right
                
        return candidate