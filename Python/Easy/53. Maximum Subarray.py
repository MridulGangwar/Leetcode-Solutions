class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float("-inf") 
        currSum = 0
        
        for num in nums:
            currSum = max(currSum+num,num)
            result = max(result,currSum)
        
        return result
		
		
		
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sumArray = 0
        result=list()
        
        for num in nums:
            if num>num+sumArray:
                sumArray=num
            else:
                sumArray+=num
            result.append(sumArray)
        return max(result)