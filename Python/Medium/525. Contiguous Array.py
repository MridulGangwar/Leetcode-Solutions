class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count,max_length = 0,0
        counts={}
        
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            else:
                count+=1
                
            if count==0:
                max_length=i+1
                
            if count not in counts:
                counts[count]=i
            else:
                max_length = max(max_length,i-counts[count])
                
                    
        return max_length
                
            
        