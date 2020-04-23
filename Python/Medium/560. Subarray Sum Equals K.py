class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumArray = []
        sumArray.append(0)
        
        for i in range(len(nums)):
            sumArray.append(sumArray[i]+nums[i])
            
        count={}
        result = 0
        for i in sumArray:
            if i-k in count:
                result+=count[i-k]
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            
                
        return result