from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        count_p,count_s = Counter(p),Counter()
        len_s, len_p = len(s), len(p)
        result=[]
        
        if len_s < len_p:
            return result
        
        for idx in range(len_s):
            count_s[s[idx]]+=1
            if idx >= len_p:
                if count_s[s[idx-len_p]]==1:
                    del count_s[s[idx-len_p]]
                else:
                    count_s[s[idx-len_p]]-=1
            
            if count_p==count_s:
                result.append(idx-len_p+1)
                
        return result