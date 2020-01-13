class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        
        for i in A:
            if i not in dic:
                dic[i]=1
            else: dic[i]+=1
                
        for key in sorted(dic.keys(),reverse=True):
            if dic[key]==1:
                return key
        
        return -1