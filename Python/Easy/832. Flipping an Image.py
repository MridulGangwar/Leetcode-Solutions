class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        func = lambda x: 0 if x==1 else 1
        for row in A:
            result.append(list(map(func,row[::-1])))
            
        return result
            