class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        r = [0]*n
        c = [0]*m
        
        for (ri,ci) in indices:
            r[ri]+=1
            c[ci]+=1
        
        odd=0
        
        for i in r:
            for j in c:
                if ((i+j)%2)==1:
                    odd+=1
        return odd
        