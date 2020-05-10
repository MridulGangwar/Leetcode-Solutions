class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        left,right = 1, num
        
        while left<= right:
            mid = left+(right-left)//2
            midSqr = mid*mid
            
            if midSqr == num:
                return True
            elif midSqr < num:
                left=mid+1
            else:
                right=mid-1
                
        return False
            
        
        
        