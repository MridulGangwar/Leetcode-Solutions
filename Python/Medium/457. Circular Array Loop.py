class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        def find_next_index(is_forward,index):
            
            direction = nums[index]>=0
            if is_forward!=direction:
                return -1
            
            next_index = (index + nums[index])%len(nums)
            if next_index==index:
                return -1
            
            return next_index
        
        for i in range(len(nums)):
            
            is_forward = nums[i]>=0
            slow,fast = i , i
            
            while True:
                
                slow = find_next_index(is_forward,slow)
                fast = find_next_index(is_forward,fast)
                
                if fast!=-1:
                    fast = find_next_index(is_forward,fast)
                    
                if slow==-1 or fast ==-1 or slow==fast:
                    break
                    
            if slow!=-1 and slow==fast:
                return True
            
        return False