class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_diff = math.inf
        
        for curr in range(len(nums)-2):
            left,right = curr+1, len(nums)-1
            while left < right:
                sumR = nums[curr] + nums[left] + nums[right]
                diff = target - sumR
                
                if diff == 0:
                    return target
                
                if diff > 0:
                    left+=1
                else:
                    right-=1
                    
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                    
        return target - min_diff