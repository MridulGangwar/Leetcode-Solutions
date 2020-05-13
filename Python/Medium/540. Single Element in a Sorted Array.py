Approach 1 O(n) time complexity

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
            elif count==1 and nums[i]!=nums[i+1]:
                return nums[i]
            else:
                count=1
                
        return nums[len(nums)-1]
		


Approach 2 O(log n) time complexity

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = low + (high-low)//2
            is_true = (high - mid)%2==0
            
            if nums[mid]==nums[mid+1]:
                if is_true==1:
                    low=mid+2
                else:
                    high=mid-1
            elif nums[mid]==nums[mid-1]:
                if is_true==1:
                    high=mid-2
                else:
                    low=mid+1
            else:
                return nums[mid]
            
        return nums[low]