class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result,index=0,0
        
        while index<len(nums):
            result+=nums[index]
            index+=2
        
        return result
        