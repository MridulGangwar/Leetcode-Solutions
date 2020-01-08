class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        result=set(mat[0])
        
        for row in mat[1:]:
            result = result & set(row)
        
        if len(result)>0:
            return min(result)
        else: return -1