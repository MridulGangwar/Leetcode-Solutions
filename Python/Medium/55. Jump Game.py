class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        goodIndex=len(nums)-1
        for index in range(len(nums)-1,-1,-1):
            if index+nums[index]>=goodIndex:
                goodIndex=index
                
        return goodIndex==0