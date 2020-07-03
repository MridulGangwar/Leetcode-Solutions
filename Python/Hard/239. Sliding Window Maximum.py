class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums)<k:
            return max(nums)
        else:
            wm = max(nums[:k])
        
        ws,result = 0,[]
        result.append(wm)
        for we in range(len(nums)):
            
            if we>=k:
                temp = nums[ws]
                ws+=1
                if nums[we]>wm:
                    wm = nums[we]
                elif temp==wm:
                    wm = max(nums[ws:we+1])
                result.append(wm)
        
        return result