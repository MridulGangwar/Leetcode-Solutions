class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        index=0
        
        while index<len(nums)-1:
            if nums[index]==nums[index+1]:
                index+=2
            else:
                return nums[index]
        return nums[len(nums)-1]
        
        