class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fib =[0,1]
        
        if N == 0:
            return 0
        
        for i in range(1,N):
            temp = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = temp
            
        return fib[1]