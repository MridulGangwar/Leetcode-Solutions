class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ws, max_length, max_letter_count = 0,0,0
        freqMap = {}
        
        for we in range(len(s)):
            ch = s[we]
            
            if ch not in freqMap:
                freqMap[ch]=0
            freqMap[ch]+=1
            
            max_letter_count = max(max_letter_count,freqMap[ch])
            
            if we-ws+1-max_letter_count>k:
                left = s[ws]
                freqMap[left]-=1
                ws+=1
                
            max_length = max(max_length,we-ws+1)
            
        return max_length