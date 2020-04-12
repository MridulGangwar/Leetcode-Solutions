# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def height(node):
            
            if not node:
                return 0
            
            lheight = height(node.left)
            rheight = height(node.right)
            
            self.res = max(self.res,lheight+rheight)
            return max(lheight,rheight)+1
        
        height(root)
        return self.res