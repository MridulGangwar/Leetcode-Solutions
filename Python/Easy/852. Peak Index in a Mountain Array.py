class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index=0
        maxOfList = A[0]
        
        for i in range(1,len(A)):
            if A[i]>maxOfList:
                maxOfList=A[i]
                index=i
                
        return index