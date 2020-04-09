class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        
        for i in A:
            result.append(i**2)
            
        result.sort()
            
        return result