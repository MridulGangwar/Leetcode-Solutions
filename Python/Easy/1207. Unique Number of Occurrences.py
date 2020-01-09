class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = {}
        
        for i in arr:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        temp=[]
        
        for key,value in counter.iteritems():
            temp.append(value)
        
        dic ={}
        
        for i in temp:
            if i in dic:
                return False
            else:
                dic[i]=1
        return True
            