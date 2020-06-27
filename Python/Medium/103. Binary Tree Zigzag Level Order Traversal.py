# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        def traverse(root,level):
            
            if root is None:
                return None
            if len(result)==level:
                result.append([])
            if level%2==1:
                result[level].insert(0,root.val)
            else:
                result[level].append(root.val)
            
            traverse(root.left,level+1)
            traverse(root.right,level+1)
            
        result=[]
        if root:
            traverse(root,0)
        return result