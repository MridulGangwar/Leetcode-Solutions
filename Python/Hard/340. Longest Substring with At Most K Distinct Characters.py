class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        ws, freM, result = 0, {}, 0
        
        for we in range(len(s)):
            ch = s[we]
            
            if ch not in freM:
                freM[ch]=0
            freM[ch]+=1
            
            while len(freM)>k:
                
                if freM[s[ws]] ==1:
                    del freM[s[ws]]
                else:
                    freM[s[ws]]-=1
                    
                ws+=1
                
            result = max(result,we-ws+1)
            
        return result