class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', 
               '}':'{', 
               ']':'['}
        result=[]
        
        if len(s)%2==1:
            return False
        
        for ch in s:
            if ch in dic and result:
                if result[-1]==dic[ch]:
                    result.pop()
            else:
                result.append(ch)
        
        if result:
            return False
        else:
            return True