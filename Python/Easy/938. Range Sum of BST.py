# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def search(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    search(node.left)
                if node.val < R:
                    search(node.right)
        self.ans=0
        search(root)
        return self.ans
                    
        