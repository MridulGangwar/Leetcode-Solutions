class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, count = 0,0
        for char in s:
            count+=1 if char=='L' else -1
            
            if count==0:
                result+=1
        return result