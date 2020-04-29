class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0 , len(nums)-1
        
        while left<right:
            midpoint = left + int((right-left)/2)
            if nums[midpoint]>nums[right]:
                left=midpoint+1
            else:
                right=midpoint
                
        return nums[left]
        