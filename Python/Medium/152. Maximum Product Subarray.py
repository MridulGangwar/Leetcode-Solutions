class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxp, minp, best =1,1, float("-inf")
        
        for num in nums:
            if num<0:
                maxp,minp = minp,maxp
            elif num==0:
                pass
            maxp = max(maxp*num,num)
            minp = min(minp*num,num)
            
            best = max(maxp,best)
            
        return best