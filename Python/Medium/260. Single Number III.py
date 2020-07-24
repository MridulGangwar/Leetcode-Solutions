#method 1
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        count=1
        result=[]
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1] and count==2:
                count=1
            elif nums[i]!=nums[i+1] and count==1:
                result.append(nums[i])
            elif nums[i]==nums[i+1]:
                count+=1
                
            if len(result)==2:
                return result
            
        result.append(nums[-1])
        
        if len(result)==1:
            result.append(0)
            
        return result
		
		
#Method 2
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return [0,0]
        
        l = []
        for num in nums:
            if num in l:
                l.remove(num)
            else:
                l.append(num)
        
        if len(l)==1:
            l.append(0)
            
        return l