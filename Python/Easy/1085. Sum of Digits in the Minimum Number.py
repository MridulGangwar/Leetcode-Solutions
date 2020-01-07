class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        minimal = min(A)
        sumOfDigit=0
        
        while minimal>0:
            sumOfDigit+=(minimal%10)
            minimal=(minimal//10)
        
        if sumOfDigit%2==0:
            return 1
        else:
            return 0   