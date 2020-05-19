from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        lens1,lens2 = len(s1),len(s2)
        if lens2<lens1:
            return False
        
        counts1 = Counter(s1)
        counts2 = Counter()
        
        for i in range(len(s2)):
            counts2[s2[i]]+=1
            
            if i>=lens1:
                if counts2[s2[i-lens1]]==1:
                    del counts2[s2[i-lens1]]
                else:
                    counts2[s2[i-lens1]]-=1
                
            if counts1==counts2:
                return True
            
        return False