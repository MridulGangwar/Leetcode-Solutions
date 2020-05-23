class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch]=1
            else:
                dic[ch]+=1
                
        result = ""
        dic1 = sorted(dic.items(),key = lambda x:x[1],reverse=True)
        
        for key,val in dic1:
            result+=(val*key)
            
        return result
        