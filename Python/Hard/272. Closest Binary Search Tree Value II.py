from heapq import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        maP, stack, he, count = {}, [], [], 0
        stack.append(root)
        while stack:
            node = stack.pop()
            diff = abs(node.val - target)
            
            if count<k:
                if diff not in maP:
                    maP[diff] = list()
                maP[diff].append(node.val)
                heappush(he,-diff)
                count+=1
            else:
                temp = -heappop(he)
                if temp>diff:
                    del maP[temp]
                    if diff not in maP:
                        maP[diff] = list()
                    maP[diff].append(node.val)
                    heappush(he,-diff)
                else:
                    heappush(he,-temp)
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                               
        return [item for sublist in maP.values() for item in sublist] 