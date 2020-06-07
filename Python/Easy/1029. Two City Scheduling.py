class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs,key = lambda x: x[0]-x[1])
        
        result=0
        n = len(costs)/2
        
        for idx in range(len(costs)):
            if idx<n:
                result+=costs[idx][0]
            else:
                result+=costs[idx][1]
                
        return result