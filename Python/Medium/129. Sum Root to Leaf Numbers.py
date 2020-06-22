# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root,0)
    
    def dfs(self,root,rsum):
        if root is None:
            return 0
        
        rsum = rsum*10 + root.val
        
        if root.left is None and root.right is None:
            return rsum
        
        return self.dfs(root.left,rsum)+self.dfs(root.right,rsum)
            
        