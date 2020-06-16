Using recursion:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root == None or root.val==val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
			
			
Using iteration:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        curr = root
        while curr != None:
            if curr.val==val: return curr
            if curr.val>val:
                curr = curr.left
            else:
                curr = curr.right
                
        return curr