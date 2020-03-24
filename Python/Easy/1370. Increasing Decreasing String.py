class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        inp = list(s)
        result=[]
        
        while len(inp)>0:
            
            smallest = sorted(set(inp))
            for small in smallest:
                result.append(small)
                inp.remove(small)
                
            largest = sorted(set(inp),reverse=True)
            for l in largest:
                result.append(l)
                inp.remove(l)
                
        return ''.join(result)