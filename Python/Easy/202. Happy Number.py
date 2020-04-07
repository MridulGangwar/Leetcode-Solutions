class Solution:
    def isHappy(self, n: int) -> bool:
        
        while True:
            sumOfDigit=0
            for i in str(n):
                sumOfDigit+=(int(i)**2)
            n = sumOfDigit
            
            if n==1 or n==7:
                return True
            elif n<10:
                return False
				
				
				
Solution 2

class Solution:
    def isHappy(self, n: int) -> bool:
        
        sumOfDigit=0
        for i in str(n):
            sumOfDigit+=(int(i)**2)
        
        
        if sumOfDigit==1 or sumOfDigit==7:
            return True
        elif sumOfDigit<10:
            return False
        else:
            return self.isHappy(sumOfDigit)