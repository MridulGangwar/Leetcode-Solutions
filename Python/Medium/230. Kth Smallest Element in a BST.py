# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            
            if root is None:
                return []
            
            left_node = inorder(root.left)
            root_node = [root.val]
            right_node = inorder(root.right)
            
            return left_node+root_node+right_node
        
        return inorder(root)[k-1]