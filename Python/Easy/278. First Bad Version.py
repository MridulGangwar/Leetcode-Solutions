# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start,end = 1 , n
        
        while start<end:
            midpoint = start + int((end-start)/2)
            if isBadVersion(midpoint):
                end = midpoint
            else:
                start=midpoint+1
        
        return start