class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        result=0
        index=0
        
        while result<5000 and index<len(arr):
            result+=arr[index]
            index+=1
            
        if result>5000:
            return index-1
        else: return index