class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        num = N
        deg = len(str(N))
        prod = 0
        
        while num > 0:
            prod = prod + (num%10)**deg
            num =num//10
            
        if prod==N:
            return True
        else: return False
        