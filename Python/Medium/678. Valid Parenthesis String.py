class Solution:
    def checkValidString(self, s: str) -> bool:
        
        count=0
        
        for i in s:
            if i==')':
                count+=1
            else:
                count-=1
                
            if count>0:
                return False
        
        if count==0:
            return True
        count=0
            
        for i in s[::-1]:
            if i=='(':
                count+=1
            else:
                count-=1
                
            if count>0:
                return False
                
        return True