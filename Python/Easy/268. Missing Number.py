class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        sumNum,n = 0, len(nums)
        for num in nums:
            sumNum+=num
            
        return (n*(n+1))/2 - sumNum        