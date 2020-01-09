class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right+1):
            if self.selfdiv(i):
                result.append(i)
        return result
            
    def selfdiv(self,num):
        
        if '0' in str(num):
            return 0
        
        temp = num
        while temp>0:
            digit = temp %10
            if (num % digit)!=0:
                return 0
            temp = temp//10
        return 1