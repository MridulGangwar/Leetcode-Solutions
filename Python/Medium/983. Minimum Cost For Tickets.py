class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        dp = [365*costs[0]]*(n+1)
        dp[n] = 0
        
        for i in range(n-1,-1,-1):
            d7,d30 = i,i
            while d7<n and days[d7]<days[i]+7: d7+=1
            while d30<n and days[d30]<days[i]+30: d30+=1
            
            dp[i] = min(costs[0]+dp[i+1],costs[1]+dp[d7],costs[2]+dp[d30])
            
        return dp[0]
        
		
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0]*len(days)
        minCost = self.traverse(days,costs,0,dp)
        return minCost
    
    def traverse(self,days,costs,idx,dp):
        if idx>=len(days):
            return 0
        if dp[idx]>0:
            return dp[idx]
        op1 = costs[0]+self.traverse(days,costs,idx+1,dp)
        
        i = idx
        while i<len(days):
            if days[i]>=days[idx]+7:
                break
            i+=1
        op2 = costs[1]+self.traverse(days,costs,i,dp)
        
        i = idx
        while i<len(days):
            if days[i]>=days[idx]+30:
                break
            i+=1
            
        op3 = costs[2]+self.traverse(days,costs,i,dp)
        minV = min(op1,op2,op3)
        dp[idx]=minV
        return minV