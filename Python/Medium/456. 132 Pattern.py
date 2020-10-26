class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        n = len(nums)
        minArray = [0]*n
        minArray[0] = nums[0]
        
        for idx in range(1,len(nums)):
            minArray[idx] = min(minArray[idx-1],nums[idx])
            
        stack = []
        
        for idx in range(n-1,-1,-1):
            if nums[idx]>minArray[idx]:
                while stack and stack[-1]<=minArray[idx]:
                    stack.pop()
                    
                if stack and stack[-1]<nums[idx]:
                    return True
                
                stack.append(nums[idx])
            
        return False
            