class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff = arr[1]-arr[0]
        
        for i in range(1,len(arr)):
            temp=arr[i]-arr[i-1]
            if temp < diff:
                diff=temp
        
        result=[]
        for i in range(1,len(arr)):
            temp=arr[i]-arr[i-1]
            if temp==diff:
                result.append([arr[i-1],arr[i]])
                
        return result
                
            
        
        
        