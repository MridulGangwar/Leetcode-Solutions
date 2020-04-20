class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums)==0:
            return -1
        
        left,right = 0, len(nums)-1
        
        while left < right:
            midpoint = left + int((right-left)/2)
            if nums[midpoint] > nums[right]:
                left=midpoint+1
            else:
                right=midpoint
                
        start=left
        left,right = 0, len(nums)-1
        
        if nums[start]<=target and nums[right]>=target:
            left=start
        else:
            right=start
        
        while left<=right:
            midpoint = left + int((right-left)/2)
            
            if nums[midpoint]== target:
                return midpoint
            elif nums[midpoint] > target:
                right = midpoint-1
            else:
                left=midpoint+1
                
        return -1
            