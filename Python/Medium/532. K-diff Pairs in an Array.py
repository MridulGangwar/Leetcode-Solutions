class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left, right, count =0, 1, 0
        
        while left < len(nums) and right < len(nums):
            if left==right or nums[right]-nums[left]<k:
                right+=1
            elif nums[right]-nums[left]>k:
                left+=1
            else:
                left+=1
                right+=1
                count+=1
                while left<len(nums) and nums[left]==nums[left-1]:
                    left+=1
        
        return count
                