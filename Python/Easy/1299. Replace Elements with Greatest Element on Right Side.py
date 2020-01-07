class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr)==1: return [-1]
        
        init = max(arr[1:])
        result=[]
        
        for i in range(len(arr)-1):
            if arr[i] == init:
                init = max(arr[i+1:])
            result.append(init)
        result.append(-1)
        
        return result
            
        
        