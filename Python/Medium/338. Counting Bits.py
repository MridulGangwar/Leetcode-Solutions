class Solution:
    def countBits(self, num: int) -> List[int]:
        
        dp = []
        dp.append(0)
        
        for i in range(1,num+1):
            dp.append(dp[i>>1] + int(i&1))
            
        return dp
		
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        result = []
        
        for i in range(num+1):
            result.append(bin(i)[2:].count("1"))
            
        return result