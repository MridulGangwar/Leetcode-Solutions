class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i,n in enumerate(A):
            if i==n:
                return i
        return -1