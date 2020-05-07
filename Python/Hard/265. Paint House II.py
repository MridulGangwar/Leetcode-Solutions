#Approach 1


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        if costs is None or len(costs)==0:
            return 0
        
        for i in range(1,len(costs)):
            for k in range(len(costs[i])):
                if k==0:
                    costs[i][k]+=min(costs[i-1][k+1:])
                elif k==len(costs[i])-1:
                    costs[i][k]+=min(costs[i-1][:k])
                else:
                    costs[i][k] += min(min(costs[i-1][0:k]),min(costs[i-1][k+1:]))
                
        return min(costs[len(costs)-1])
        
		
		
#Approach 2

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        if costs is None or len(costs)==0:
            return 0
        
        for house in range(1,len(costs)):
            min_cost = second_min_cost = float('inf')
            loc = 0
            
            for k in range(len(costs[0])):
                if costs[house-1][k]<min_cost:
                    second_min_cost = min_cost
                    min_cost = costs[house-1][k]
                    loc=k
                elif costs[house-1][k]<second_min_cost:
                    second_min_cost = costs[house-1][k]
                    
            for k in range(len(costs[0])):
                if k==loc:
                    costs[house][k]+=second_min_cost
                else:
                    costs[house][k]+=min_cost
            
        return min(costs[len(costs)-1]) 
        
        