from collections import defaultdict 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return None
        
        result = defaultdict(list)
        queue = deque([(root,0)])
        
        while queue:
            node, col = queue.popleft()
            result[col].append(node.val)
            
            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
                
        return [result[x] for x in sorted(result.keys())]