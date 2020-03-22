class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort= sorted(nums)
        result = []
        
        for index in range(len(nums)):
            result.append(nums_sort.index(nums[index]))
        return result