##Approach 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        
        left, right = 0,len(height)-1
        
        while left < right:
            maxArea = max(maxArea,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return maxArea
		
##Approach 2

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        
        left, right = 0,len(height)-1
        
        while left < right:
            w = right-left
            
            if height[left] < height[right]:
                h = height[left]
                left+=1
            else:
                h = height[right]
                right-=1
                
            area = h*w
            if area>maxArea:
                maxArea = area 
                
        
        return maxArea
        