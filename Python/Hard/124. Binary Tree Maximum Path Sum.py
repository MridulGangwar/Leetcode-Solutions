# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathS=float('-inf')
        
        def pathSum(node):
            if node==None:
                return 0
            left=max(0,pathSum(node.left))
            right=max(0,pathSum(node.right))
            self.maxPathS = max(self.maxPathS,left+right+node.val)
            return max(left,right) + node.val
        
        pathSum(root)
        return self.maxPathS