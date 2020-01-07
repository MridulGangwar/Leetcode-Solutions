class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        index = 0 - (n//2)
        sum = index
        result = []
        
        while sum!=0:
            result.append(index)
            index+=1
            sum+=index
        
        result.append(index)
        
        if n%2 == 1:
            return result
        else:
            result.remove(0)
            return result