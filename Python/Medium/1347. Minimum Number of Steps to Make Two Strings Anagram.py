class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dic ={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        count=0
        for i in t:
            if i in dic and dic[i]>0:
                count+=1
                dic[i]-=1
                
        return len(s) - count
		

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dic = Counter(s)-Counter(t)
        count=0
        for key,value in dic.most_common():
            count+=value
        
        return count