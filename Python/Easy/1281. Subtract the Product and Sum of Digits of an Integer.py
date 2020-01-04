class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = n
        prod, sumofdigits =1,0
        
        while N>0:
            prod = prod * (N%10)
            sumofdigits = sumofdigits + (N%10)
            N = N//10
            
        return (prod - sumofdigits)