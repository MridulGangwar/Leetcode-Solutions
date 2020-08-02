# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(node,cumsum,maP):
            nonlocal ans
            if not node:
                return
            
            cumsum+=node.val
            if cumsum-sum in maP:
                ans+=maP[cumsum-sum]
                
            if cumsum not in maP:
                maP[cumsum]=0
            maP[cumsum]+=1
            
            dfs(node.left,cumsum,maP)
            dfs(node.right,cumsum,maP)
            
            maP[cumsum]-=1
            
            
            
        maP = {0:1}
        ans = 0
        dfs(root,0,maP)
        return ans