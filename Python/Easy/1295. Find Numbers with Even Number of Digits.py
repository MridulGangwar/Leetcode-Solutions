class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in nums:
            if len(str(i))%2==0:
                result+=1
        return result