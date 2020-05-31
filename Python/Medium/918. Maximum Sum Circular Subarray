class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        K = self.maxSubarray(A)
        CS = 0
        for idx in range(len(A)):
            CS+=A[idx]
            A[idx]=-A[idx]
        CS+=self.maxSubarray(A)
        
        if CS>K and CS!=0:
            return CS
        else:
            return K
        
    
    def maxSubarray(self,nums):  
        subS, result = nums[0],nums[0] 
        for num in nums[1:]:
            if subS+num<num:
                subS = num
            else:
                subS+=num
            if result < subS:
                result = subS
        return result    
        