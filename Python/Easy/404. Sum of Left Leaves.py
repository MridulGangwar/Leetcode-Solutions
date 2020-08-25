# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def isRoot(node):
            if node and node.left is None and node.right is None:
                return True
            return False
            
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append(root)
        sumLeft = 0
        
        while queue:
            node = queue.popleft()
            if isRoot(node.left):
                sumLeft+=node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                    
        return sumLeft
		
		
		
		

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def reverse(node,is_left):
            nonlocal sumLeft
            if node.left is None and node.right is None:
                if is_left:
                    sumLeft+=node.val
                
            if node.left:
                reverse(node.left,True)
            if node.right:
                reverse(node.right,False)
            
        sumLeft = 0
        if root:
            reverse(root,False)
                    
        return sumLeft