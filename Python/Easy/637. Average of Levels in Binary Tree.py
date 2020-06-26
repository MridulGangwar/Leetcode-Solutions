# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        def traverse(root,level):
            if len(stack)==level:
                stack.append([])
            stack[level].append(root.val)
            if root.left:
                traverse(root.left,level+1)
            if root.right:
                traverse(root.right,level+1)
            
            
        stack,result = [],[]
        if root:
            traverse(root,0)
        
        for l in stack:
            result.append(sum(l)/len(l))
            
        return result