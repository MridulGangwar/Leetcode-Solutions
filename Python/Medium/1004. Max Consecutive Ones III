class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        ws, sz, result = 0, 0 , 0
        
        for we in range(len(A)):
            
            if A[we]==0:
                sz+=1
                
            while sz>K:
                if A[ws]==0:
                    sz-=1
                ws+=1
                    
            result = max(result,we-ws+1)
            
        return result