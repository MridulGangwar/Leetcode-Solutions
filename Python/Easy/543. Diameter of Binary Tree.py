# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def dfs(node):
            nonlocal diam 
            if not node:
                return 0
            
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)
            
            diamNode = leftTree+rightTree+1
            diam = max(diamNode,diam)
            
            return max(leftTree,rightTree)+1
        
        diam = 0
        dfs(root)
        if diam:
            diam-=1
        return diam
        