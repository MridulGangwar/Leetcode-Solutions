# iteration solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack =[]
        result=[]
        if root is None:
            return result
        
        stack.append(root)
        while stack:
            temp = stack.pop()
            result.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
                
        return result[::-1]
		
		
#Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traverse(root):
            result.append(root.val)
            
            if root.right:
                traverse(root.right)
            if root.left:
                traverse(root.left)
        
        
        result=[]
        if root:
            traverse(root)
        return result[::-1]