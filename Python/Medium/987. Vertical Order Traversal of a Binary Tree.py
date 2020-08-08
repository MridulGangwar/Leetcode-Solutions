from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        def bfs(root):
            stack.append((root,0,0))
            while stack:
                node,col,row = stack.pop()
                if node:
                    node_list.append([col,row,node.val])
                    stack.append([node.left,col-1,row+1])
                    stack.append([node.right,col+1,row+1])
                    
        
        stack,node_list = [], []
        bfs(root)
        node_list.sort()
        
        result = OrderedDict()
        for col,row,val in node_list:
            if col in result:
                result[col].append(val)
            else:
                result[col]=[val]
                
        return result.values()