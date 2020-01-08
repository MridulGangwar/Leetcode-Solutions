class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic ={}
        
        for i in A:
            if i in dic:
                return i
            else:
                dic[i]=1